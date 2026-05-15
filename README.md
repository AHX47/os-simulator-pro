# OS Simulator PRO — Build Guide

## Files in this package

| File | Purpose |
|------|---------|
| `app.html` | Complete standalone app (all 4 simulators) |
| `launcher.py` | Python desktop launcher (Flask + webview) |
| `build_windows.py` | PyInstaller build script → `.exe` |
| `build_linux.py` | PyInstaller build script → Linux binary |
| `build_all.sh` | One-click Linux build pipeline |
| `build_all.bat` | One-click Windows build pipeline |

---

## Quick Build — Linux

```bash
chmod +x build_all.sh
./build_all.sh
# Output: dist/OS-Simulator-PRO
./dist/OS-Simulator-PRO
```

## Quick Build — Windows

Double-click `build_all.bat`
or in CMD:
```cmd
build_all.bat
# Output: dist\OS-Simulator-PRO.exe
```

---

## Manual Steps (any OS)

```bash
# 1. Install requirements
pip install pyinstaller flask pywebview

# 2. Linux build
python3 build_linux.py

# 3. Windows build
python build_windows.py
```

---

## How it works

```
dist/OS-Simulator-PRO(.exe)
  └── launcher.py (embedded)
        ├── Flask server  → serves app.html on localhost:RANDOM_PORT
        └── pywebview     → opens native OS window (no browser needed)
              └── app.html (embedded) → React app, all simulators
```

If `pywebview` is not available, it automatically opens in your default browser instead.

---

## Requirements

- Python 3.8+
- pip

**For native window on Linux (optional):**
```bash
sudo apt install python3-gi gir1.2-webkit2-4.0
pip install pywebview
```

**For native window on Windows:**
pywebview uses Edge/IE automatically — no extra install needed.

---

## Run without building (dev mode)

```bash
pip install flask pywebview
python3 launcher.py
```

The app opens immediately — no npm, no Node.js needed.

---

*CPU Scheduling · Page Replacement · Address Translation · Buddy System*
# os-simulator-pro
# os-simulator-pro
# os-simulator-pro
# os-simulator-pro
# os-simulator-pro
