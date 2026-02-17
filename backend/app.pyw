from flask import Flask, jsonify, request
from flask_cors import CORS
import asyncio
from led_controller import LEDController

import os

app = Flask(__name__, 
            static_folder='../frontend/dist', 
            static_url_path='/')
CORS(app)

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

if __name__ == '__main__':
    print("Iniciando servidor en http://localhost:5000")
    # Intentamos conexión inicial silenciosa
    try:
        run_async(execute_mobile_command(asyncio.sleep(0)))
    except:
        pass
    app.run(host='0.0.0.0', port=5000, debug=False)
