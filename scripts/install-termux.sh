#!/data/data/com.termux/files/usr/bin/bash
echo "[*] Installing RION MODS dependencies for Termux..."

pkg update -y
pkg upgrade -y
pkg install -y python git curl

if [ ! -d "venv" ]; then
    python -m venv venv
fi

source venv/bin/activate
pip install --upgrade pip
pip install -r server/requirements.txt

echo "[*] Installation complete! Run ./scripts/run-server.sh to start the backend."
