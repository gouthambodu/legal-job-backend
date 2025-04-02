#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Install Playwright and its browser binaries
python -m pip install playwright
python -m playwright install
