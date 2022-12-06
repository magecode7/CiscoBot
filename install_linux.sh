#!bin/sh
echo "Installing venv"
python3 -m venv .venv

echo "Installing requirements"
.venv/bin/pip3 install -r requirements.txt

.venv/bin/python3 config.py

echo "Installing completed!"