#!/usr/bin/env bash

set -e

echo "🚀 Setting up environment..."

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -e .[dev]

echo "✅ Environment ready."
echo "👉 Run: make smoke"
