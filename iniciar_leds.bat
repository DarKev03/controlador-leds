@echo off
cd /d "%~dp0"
start "" ".venv\Scripts\pythonw.exe" "backend\app.pyw"
start "" ".venv\Scripts\pythonw.exe" "Game Watcher\app.pyw"
