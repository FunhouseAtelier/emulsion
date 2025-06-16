#!/bin/bash

VENV_DIR="server/.venv"

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  source "$VENV_DIR/Scripts/activate"
else
  source "$VENV_DIR/bin/activate"
fi
