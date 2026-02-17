import asyncio
from bleak import BleakScanner, BleakClient
import constants

class LEDController:
    def __init__(self):
        self.client = None
        self.device_address = None
        self.write_uuid = constants.WRITE_UUID

    async def scan_devices(self):
        # Si ya estamos conectados, devolvemos el dispositivo actual marcado como conectado
        if self.client and self.client.is_connected:
            print("DEBUG: Ya conectado, devolviendo dispositivo actual", flush=True)
            return [{"name": "ELK-BLEDOM", "address": self.device_address, "connected": True}]
        
        # Si no, escaneamos normalmente
        print("DEBUG: Escaneando dispositivos...", flush=True)
        devices = await BleakScanner.discover()
        return [{"name": d.name, "address": d.address, "connected": False} for d in devices if d.name and "ELK" in d.name]

    async def connect(self, address):
        if self.client and self.client.is_connected:
            await self.client.disconnect()
        
        self.device_address = address
        self.client = BleakClient(address)
        await self.client.connect()
        return True

    async def disconnect(self):
        if self.client and self.client.is_connected:
            await self.client.disconnect()
        self.client = None

    async def send_command(self, data):
        if self.client and self.client.is_connected:
            print(f"DEBUG: Enviando comando BLE: {bytearray(data).hex()}", flush=True)
            await self.client.write_gatt_char(self.write_uuid, bytearray(data))
            return True
        print("DEBUG: Intento de envío fallido - No conectado", flush=True)
        return False

    async def set_color(self, r, g, b):
        # Comando de color: 0x7e 0x07 0x05 0x03 [r] [g] [b] 0x00 0xef
        command = [0x7e, 0x07, 0x05, 0x03, r, g, b, 0x00, 0xef]
        return await self.send_command(command)

    async def set_power(self, on: bool):        
        if on:
            # Comando ON real para ELK-BLEDOM
            command = [0x7e, 0x04, 0x04, 0xf0, 0x00, 0x01, 0xff, 0x00, 0xef]
        else:
            # Comando OFF real para ELK-BLEDOM
            command = [0x7e, 0x04, 0x04, 0x00, 0x00, 0x00, 0xff, 0x00, 0xef]
        
        print(f"Enviando comando {'ON' if on else 'OFF'}: {command}")
        return await self.send_command(command)
