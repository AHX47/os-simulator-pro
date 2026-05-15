@echo off
REM ─────────────────────────────────────────────────────────────────────────
REM  build_all.bat  —  Full build pipeline for OS Simulator PRO on Windows
REM  Double-click or run from CMD / PowerShell
REM ─────────────────────────────────────────────────────────────────────────
echo.
echo ╔══════════════════════════════════════════════╗
echo ║   OS Simulator PRO — Windows Build          ║
echo ╚══════════════════════════════════════════════╝
echo.

cd /d "%~dp0"

REM ── 1. Python check ────────────────────────────────────────────────────────
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found.
    echo Download from https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version

REM ── 2. Install deps ────────────────────────────────────────────────────────
echo.
echo ^> Installing dependencies...
python -m pip install --upgrade pip -q
python -m pip install pyinstaller flask pywebview -q
if %errorlevel% neq 0 (
    echo [ERROR] pip install failed.
    pause
    exit /b 1
)
echo [OK] Dependencies installed

REM ── 3. Build EXE ───────────────────────────────────────────────────────────
echo.
echo ^> Building Windows EXE...
python build_windows.py
if %errorlevel% neq 0 (
    echo [ERROR] Build failed.
    pause
    exit /b 1
)

REM ── 4. Done ────────────────────────────────────────────────────────────────
echo.
echo ╔══════════════════════════════════════════════╗
echo ║   BUILD COMPLETE                            ║
echo ╠══════════════════════════════════════════════╣
echo ║  EXE location: dist\OS-Simulator-PRO.exe    ║
echo ╚══════════════════════════════════════════════╝
echo.
pause
