"""
build_linux.py  —  Run this on Linux to produce ./dist/OS-Simulator-PRO (ELF binary)
Requires: pip install pyinstaller flask pywebview
Optional for native window: pip install pywebview  (needs GTK: sudo apt install python3-gi gir1.2-webkit2-4.0)
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

cmd = [
    sys.executable, '-m', 'PyInstaller',
    '--noconfirm',
    '--clean',
    '--onefile',                         # single binary
    '--windowed',                        # no terminal window (needs display)
    f'--name=OS-Simulator-PRO',
    f'--add-data={os.path.join(HERE,"app.html")}:.',   # bundle HTML (Linux uses : separator)
    '--hidden-import=flask',
    '--hidden-import=werkzeug',
    '--hidden-import=jinja2',
    '--hidden-import=click',
    '--hidden-import=itsdangerous',
    '--hidden-import=webview',
    '--hidden-import=threading',
    '--collect-all=webview',
    os.path.join(HERE, 'launcher.py'),
]

print('Building Linux ELF binary...')
print(' '.join(cmd))
result = subprocess.run(cmd, cwd=HERE)
if result.returncode == 0:
    bin_path = os.path.join(HERE, 'dist', 'OS-Simulator-PRO')
    os.chmod(bin_path, 0o755)
    print(f'\n✅ Done!  Output: {bin_path}')
    print('Run it with:  ./dist/OS-Simulator-PRO')
else:
    print('\n❌ Build failed. Check output above.')
    sys.exit(result.returncode)
