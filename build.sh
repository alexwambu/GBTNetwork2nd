#!/bin/bash
echo "Installing Python requirements..."
pip install -r requirements.txt

echo "Starting GBTNetwork Layer 1 UI..."
streamlit run launch.py
