#!/usr/bin/env bash
# ─────────────────────────────────────────────────────────────────────────────
# build_all.sh  —  Full build pipeline for OS Simulator PRO
# Run:  chmod +x build_all.sh && ./build_all.sh
# ─────────────────────────────────────────────────────────────────────────────
set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$DIR"

echo ""
echo "╔══════════════════════════════════════════════╗"
echo "║   OS Simulator PRO — Build Pipeline         ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

# ── 1. Python check ──────────────────────────────────────────────────────────
if ! command -v python3 &>/dev/null; then
    echo "❌ python3 not found. Install: sudo apt install python3 python3-pip"
    exit 1
fi
echo "✔ Python: $(python3 --version)"

# ── 2. Install deps ──────────────────────────────────────────────────────────
echo ""
echo "► Installing Python dependencies..."
python3 -m pip install --upgrade  --break-system-packages
python3 -m pip install pyinstaller flask pywebview  --break-system-packages

echo "✔ Dependencies installed"

# ── 3. (Optional) GTK WebKit for native window on Linux ──────────────────────
echo ""
echo "► Installing GTK WebKit2 for native window (optional, needs sudo)..."
if command -v apt &>/dev/null; then
    sudo apt install -y python3-gi gir1.2-webkit2-4.0 2>/dev/null || echo "  (skipped — run manually if you want native window)"
fi

# ── 4. Build Linux binary ───────────────────────────────────────────────────
echo ""
echo "► Building Linux binary..."
python3 build_linux.py

# ── 5. Done ─────────────────────────────────────────────────────────────────
echo ""
echo "╔══════════════════════════════════════════════╗"
echo "║   ✅ BUILD COMPLETE                          ║"
echo "╠══════════════════════════════════════════════╣"
echo "║  Binary → dist/OS-Simulator-PRO              ║"
echo "║  Run it → ./dist/OS-Simulator-PRO            ║"
echo "╚══════════════════════════════════════════════╝"
echo ""
