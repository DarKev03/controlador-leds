@echo off
cd /d "%~dp0"
echo Iniciando Controlador de LEDs en segundo plano...
start "" ".venv\Scripts\pythonw.exe" "backend\app.pyw"
echo El servidor esta arrancando.
echo Puedes acceder en: http://localhost:5000
timeout /t 2