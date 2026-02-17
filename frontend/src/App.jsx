import { useState, useEffect, useRef } from 'react'
import './App.css'

const API_BASE = window.location.origin === 'http://localhost:5173' ? 'http://127.0.0.1:5000' : window.location.origin

function App() {
  const [devices, setDevices] = useState([])
  const [scanning, setScanning] = useState(false)
  const [connectedAddr, setConnectedAddr] = useState(null)
  const [loading, setLoading] = useState(false)
  const [color, setColor] = useState('#ff00ff')
  const [isOn, setIsOn] = useState(true)

  useEffect(() => {
    scanDevices()
  }, [])

  const scanDevices = async () => {
    console.log("FETCH: Iniciando escaneo en", `${API_BASE}/scan`);
    setScanning(true)
    try {
      const resp = await fetch(`${API_BASE}/scan`)
      console.log("FETCH: Respuesta recibida", resp.status);
      const data = await resp.json()
      console.log("FETCH: Dispositivos recibidos", data);
      setDevices(data)

      // Si algún dispositivo ya está conectado en el backend, saltar directo a controles
      const alreadyConnected = data.find(d => d.connected)
      if (alreadyConnected) {
        console.log("FETCH: Dispositivo ya conectado detectado:", alreadyConnected.address);
        setConnectedAddr(alreadyConnected.address)
      }
    } catch (err) {
      console.error("FETCH ERROR: Error en el escaneo", err);
      alert("Error al conectar con el backend. ¿Está corriendo en http://127.0.0.1:5000?");
    } finally {
      setScanning(false)
    }
  }

  const connectToDevice = async (address) => {
    console.log("FETCH: Conectando a", address);
    setLoading(true)
    try {
      const resp = await fetch(`${API_BASE}/connect`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ address })
      })
      const data = await resp.json()
      console.log("FETCH: Resultado conexión", data);
      if (data.success) {
        setConnectedAddr(address)
      }
    } catch (err) {
      console.error("FETCH ERROR: Error al conectar", err);
    } finally {
      setLoading(false)
    }
  }

  const controlLED = async (action, params = {}) => {
    if (!connectedAddr) return
    try {
      await fetch(`${API_BASE}/control`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ action, ...params })
      })
    } catch (err) {
      console.error("Control failed", err)
    }
  }

  const lastSent = useRef(0)
  const handleColorChange = (e) => {
    const newColor = e.target.value
    setColor(newColor)

    // Throttle: solo enviar un comando cada 100ms para no saturar el Bluetooth
    const now = Date.now()
    if (now - lastSent.current < 100) return
    lastSent.current = now

    // Convert hex to RGB
    const r = parseInt(newColor.slice(1, 3), 16)
    const g = parseInt(newColor.slice(3, 5), 16)
    const b = parseInt(newColor.slice(5, 7), 16)
    controlLED('color', { r, g, b })
  }

  const togglePower = () => {
    const newState = !isOn
    setIsOn(newState)
    controlLED('power', { value: newState })
  }

  return (
    <div className="container">
      <h1>ELK LED Controller</h1>

      <div className="card">
        <button
          className="button"
          onClick={scanDevices}
          disabled={scanning}
        >
          {scanning ? 'Escaneando...' : 'Buscar LEDs'}
        </button>

        <ul className="device-list">
          {devices.map(device => (
            <li
              key={device.address}
              className={`device-item ${connectedAddr === device.address ? 'active' : ''}`}
            >
              <div>
                <strong>{device.name}</strong>
                <br />
                <small>{device.address}</small>
              </div>
              <button
                className="button"
                onClick={() => connectToDevice(device.address)}
                disabled={loading || connectedAddr === device.address}
              >
                {connectedAddr === device.address ? 'Conectado' : 'Conectar'}
              </button>
            </li>
          ))}
          {devices.length === 0 && !scanning && <p>No se encontraron dispositivos</p>}
        </ul>
      </div>

      {connectedAddr && (
        <div className="controls">
          <div className="color-picker-wrapper">
            <input
              type="color"
              value={color}
              onChange={handleColorChange}
            />
          </div>

          <button
            className={`button power-btn ${isOn ? '' : 'off'}`}
            onClick={togglePower}
            style={{ filter: isOn ? 'drop-shadow(0 0 10px #7c3aed)' : 'none' }}
          >
            {isOn ? 'ON' : 'OFF'}
          </button>
        </div>
      )}
    </div>
  )
}

export default App
