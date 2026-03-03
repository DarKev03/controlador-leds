from flask import Flask, jsonify, request
from flask_cors import CORS
import asyncio
from led_controller import LEDController

import os
import threading
import win32gui
import win32con
import win32api

app = Flask(__name__, 
            static_folder='../frontend/dist', 
            static_url_path='/')
CORS(app)

import constants

@app.route('/')
def serve_index():
    return app.send_static_file('index.html')

controller = LEDController()

@app.before_request
def log_request_info():
    print(f">>> API REQUEST: {request.method} {request.path}", flush=True)

def run_async(coro):
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    return loop.run_until_complete(coro)

async def execute_mobile_command(coro):
    """Helper to ensure connection and execute command in one async transaction."""
    if not controller.client or not controller.client.is_connected:
        print(f"Mobile API: Auto-conexión a {constants.MAC_ADDRESS}")
        await controller.connect(constants.MAC_ADDRESS)
    return await coro

@app.route('/scan', methods=['GET'])
def scan():
    print("API: Recibida petición de escaneo", flush=True)
    devices = run_async(controller.scan_devices())
    print(f"API: Escaneo completado. Encontrados: {len(devices)}", flush=True)
    return jsonify(devices)

@app.route('/connect', methods=['POST'])
def connect():
    data = request.json
    address = data.get('address')
    print(f"API: Intentando conectar a: {address}", flush=True)
    if not address:
        return jsonify({"error": "No address provided"}), 400
    
    success = run_async(controller.connect(address))
    print(f"API: Resultado conexión: {success}", flush=True)
    return jsonify({"success": success})

@app.route('/control', methods=['POST'])
def control():
    data = request.json
    action = data.get('action')
    print(f"API: Recibido comando de control: {action}", flush=True)
    
    if action == 'color':
        r = data.get('r', 0)
        g = data.get('g', 0)
        b = data.get('b', 0)
        success = run_async(controller.set_color(r, g, b))
    elif action == 'power':
        on = data.get('value', False)
        success = run_async(controller.set_power(on))
    else:
        return jsonify({"error": "Invalid action"}), 400
    
    print(f"API: Comando procesado con éxito: {success}", flush=True)
    return jsonify({"success": success})

# --- Mobile Endpoints for iPhone Shortcuts ---

@app.route('/mobile/encender', methods=['GET'])
def mobile_on():
    success = run_async(execute_mobile_command(controller.set_power(True)))
    return jsonify({"success": success})

@app.route('/mobile/apagar', methods=['GET'])
def mobile_off():
    success = run_async(execute_mobile_command(controller.set_power(False)))
    return jsonify({"success": success})

@app.route('/mobile/relax', methods=['GET'])
def mobile_relax():
    success = run_async(execute_mobile_command(controller.set_color(255, 100, 0)))
    return jsonify({"success": success})

@app.route('/mobile/hot', methods=['GET'])
def mobile_hot():
    success = run_async(execute_mobile_command(controller.set_color(255, 0, 0)))
    return jsonify({"success": success})

@app.route('/mobile/cold', methods=['GET'])
def mobile_cold():
    success = run_async(execute_mobile_command(controller.set_color(0, 255, 255)))
    return jsonify({"success": success})

def shutdown_handler_window():
    """Create a hidden window to listen for session end messages."""
    def on_session_end(hwnd, msg, wparam, lparam):
        if msg == win32con.WM_QUERYENDSESSION or msg == win32con.WM_ENDSESSION:
            print(">>> SHUTDOWN DETECTED. Sending OFF command to LEDs...", flush=True)
            try:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(controller.connect(constants.MAC_ADDRESS))
                loop.run_until_complete(controller.set_power(False))
                loop.run_until_complete(controller.disconnect())
                print(">>> LEDs turned off successfully during shutdown.", flush=True)
            except Exception as e:
                print(f">>> Failed to turn off LEDs during shutdown: {e}", flush=True)
            return True
        return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

    wc = win32gui.WNDCLASS()
    wc.lpfnWndProc = on_session_end
    wc.lpszClassName = "LEDControllerShutdownListener"
    wc.hInstance = win32api.GetModuleHandle(None)
    
    try:
        class_atom = win32gui.RegisterClass(wc)
        hwnd = win32gui.CreateWindow(
            class_atom, "Shutdown Listener", 0, 0, 0, 0, 0, 0, 0, wc.hInstance, None
        )
        print(">>> Shutdown listener window created", flush=True)
        win32gui.PumpMessages()
    except Exception as e:
        print(f">>> Error in shutdown handler window: {e}", flush=True)

if __name__ == '__main__':    
    
    # Iniciar el hilo de escucha de apagado
    shutdown_thread = threading.Thread(target=shutdown_handler_window, daemon=True)
    shutdown_thread.start()

    # Intentamos conexión inicial silenciosa
    try:
        run_async(execute_mobile_command(asyncio.sleep(0)))
    except:
        pass
    app.run(host='0.0.0.0', port=5000, debug=False)
