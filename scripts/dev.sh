#!/bin/bash

case "$1" in
  server)
    echo "🔧 Starting FastAPI backend..."
    PYTHONPATH=. server/.venv/bin/python -m uvicorn server.main:app --reload --host 0.0.0.0 --port 8080
    ;;
  client)
    echo "🎨 Starting Vite frontend..."
    vite
    ;;
  *)
    echo "🚀 Starting both client + server..."
    concurrently \
      "npm run dev server" \
      "npm run dev client"
    ;;
esac
