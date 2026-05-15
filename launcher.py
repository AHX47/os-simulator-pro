"""
OS Simulator PRO — Desktop Launcher
Works on Windows, Linux, macOS.
Embeds the full HTML app and serves it via Flask in a native window.
"""
import sys
import os
import threading
import time
import webbrowser
import socket

# ── Resolve bundled HTML path (works both dev and PyInstaller) ──────────────
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_PATH = os.path.join(BASE_DIR, 'app.html')

# ── Flask micro-server ───────────────────────────────────────────────────────
from flask import Flask, send_file, Response
import mimetypes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'os-sim-pro-2026'

@app.route('/')
def index():
    return send_file(HTML_PATH)

@app.route('/favicon.ico')
def favicon():
    return Response('', status=204)

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

PORT = find_free_port()
URL  = f'http://127.0.0.1:{PORT}'

def run_server():
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)          # silence Flask output
    app.run(host='127.0.0.1', port=PORT, threaded=True)

# ── Try native webview window, fall back to system browser ──────────────────
def launch():
    # Start Flask in background
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(0.6)   # let the server bind

    # Attempt pywebview first (gives a real native window)
    try:
        import webview
        webview.create_window(
            'OS Simulator PRO',
            URL,
            width=1280,
            height=800,
            min_size=(900, 600),
            background_color='#0A0B10',
        )
        webview.start()
        return
    except Exception:
        pass

    # Attempt tkinter + embedded browser (Windows IE/Edge backend)
    try:
        import tkinter as tk
        try:
            from tkinterweb import HtmlFrame
            root = tk.Tk()
            root.title('OS Simulator PRO')
            root.geometry('1280x800')
            root.configure(bg='#0A0B10')
            frame = HtmlFrame(root, messages_enabled=False)
            frame.load_url(URL)
            frame.pack(fill='both', expand=True)
            root.mainloop()
            return
        except ImportError:
            pass
    except Exception:
        pass

    # Last resort: open in the default system browser and keep process alive
    print(f'[OS Simulator PRO] Opening at {URL}')
    webbrowser.open(URL)
    print('Press Ctrl+C to quit.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    launch()
