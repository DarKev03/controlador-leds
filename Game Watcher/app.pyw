import time
import ctypes
import requests
import constants

def get_active_window_title():
    """Devuelve el título de la ventana activa en Windows."""
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    if length == 0:
        return ""
    buf = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buf, length + 1)
    return buf.value


def match_game(window_title):
    """Busca si el título de la ventana contiene el nombre de algún juego."""
    title_lower = window_title.lower()
    for game_name in constants.GAME_COLORS:
        if game_name == "default":
            continue
        if game_name.lower() in title_lower:
            return game_name
    return None


def set_color(color):
    """Envía el color al endpoint de Flask."""
    try:
        requests.post(constants.FLASK_URL, json={
            "action": "color",
            "r": color["r"],
            "g": color["g"],
            "b": color["b"],
        }, timeout=2)
    except requests.exceptions.ConnectionError:
        print("⚠️  No se pudo conectar con Flask. ¿Está corriendo?")
    except Exception as e:
        print(f"⚠️  Error enviando color: {e}")


def main():
    print("🎮 Game Watcher iniciado")
    current_game = None

    while True:
        title = get_active_window_title()
        matched_game = match_game(title)

        if matched_game != current_game:
            current_game = matched_game
            color = constants.GAME_COLORS.get(matched_game, constants.GAME_COLORS["default"])

            if matched_game:
                print(f"🎮 Juego detectado: {matched_game} → RGB({color['r']}, {color['g']}, {color['b']})")
            else:
                print(f"🖥️  Sin juego activo → color por defecto")

            set_color(color)

        time.sleep(constants.POLL_INTERVAL)


if __name__ == "__main__":
    main()