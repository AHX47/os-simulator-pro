"""
build_windows.py  —  Run this on Windows to produce OS-Simulator-PRO.exe
Requires: pip install pyinstaller flask pywebview
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

cmd = [
    sys.executable, '-m', 'PyInstaller',
    '--noconfirm',
    '--clean',
    '--onefile',                         # single .exe
    '--windowed',                        # no console window
    f'--name=OS-Simulator-PRO',
    f'--add-data={os.path.join(HERE,"app.html")};.',   # bundle HTML (Windows uses ; separator)
    '--hidden-import=flask',
    '--hidden-import=werkzeug',
    '--hidden-import=jinja2',
    '--hidden-import=click',
    '--hidden-import=itsdangerous',
    '--hidden-import=webview',
    '--hidden-import=threading',
    '--collect-all=webview',
    '--icon=icon.ico',                   # optional: place icon.ico next to this script
    os.path.join(HERE, 'launcher.py'),
]

print('Building Windows EXE...')
print(' '.join(cmd))
result = subprocess.run(cmd, cwd=HERE)
if result.returncode == 0:
    print('\n✅ Done!  Output: dist/OS-Simulator-PRO.exe')
else:
    print('\n❌ Build failed. Check output above.')
    sys.exit(result.returncode)
