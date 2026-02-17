# ELK-BLEDOM LED Controller

A web-based and voice-controlled interface for ELK-BLEDOM Bluetooth LED strips. Control your lights from your browser or via iPhone Shortcuts with ease.

[English](#english) | [Español](#español)

---

## English

### ✨ Features
- **Auto-Connect**: Automatically connects to your LEDs using the saved MAC address.
- **Web Interface**: Modern React-based UI for color selection and power toggle.
- **iPhone Integration**: dedicated endpoints for iOS Shortcuts and Siri voice commands.
- **Background Mode**: Run it as a background service on Windows.

### 🚀 Quick Start
1. **Requirements**: Python 3.9+ and Bluetooth-enabled PC.
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Configure**: Update `MAC_ADDRESS` in `backend/constants.py`.
4. **Run**: Execute `python backend/app.py` and open `http://localhost:5000`.

### 📱 iOS Shortcuts
Create a "Get Contents of URL" shortcut pointing to:
- `http://<YOUR_PC_IP>:5000/mobile/relax` (Amber)
- `http://<YOUR_PC_IP>:5000/mobile/hot` (Red)
- `http://<YOUR_PC_IP>:5000/mobile/cold` (Cyan)

---

## Español

### ✨ Características
- **Auto-Conexión**: Conexión automática usando la dirección MAC guardada.
- **Interfaz Web**: UI moderna en React para elegir colores y encendido.
- **Integración iPhone**: Endpoints dedicados para Atajos de iOS y comandos de voz de Siri.
- **Modo Fondo**: Ejecución silenciosa como servicio en Windows.

### 🚀 Inicio Rápido
1. **Requisitos**: Python 3.9+ y PC con Bluetooth.
2. **Instalar dependencias**: `pip install -r requirements.txt`
3. **Configurar**: Edita `MAC_ADDRESS` en `backend/constants.py`.
4. **Ejecutar**: Lanza `python backend/app.py` y entra en `http://localhost:5000`.

### 📱 Atajos de iOS
Crea un atajo de "Obtener contenido de URL" hacia:
- `http://<TU_IP_PC>:5000/mobile/relax` (Ámbar)
- `http://<TU_IP_PC>:5000/mobile/hot` (Rojo)
- `http://<TU_IP_PC>:5000/mobile/cold` (Cian)

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask, Bleak (Bluetooth Low Energy)
- **Frontend**: React, Vite, CSS3
- **DevOps**: Windows Startup integration (.pyw)

## 📄 License
MIT License - Feel free to use and modify for your personal projects!
