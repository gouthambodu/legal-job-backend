#!/bin/bash

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install fastapi uvicorn requests beautifulsoup4 playwright

echo "Installing Playwright browser binaries..."
python -m playwright install
