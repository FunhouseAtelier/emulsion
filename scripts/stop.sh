#!/bin/bash

kill_process() {
  pgrep -f "$1" | xargs -r kill
}

case "$1" in
  server)
    echo "🛑 Stopping FastAPI backend..."
    kill_process "uvicorn"
    ;;
  client)
    echo "🛑 Stopping Vite frontend..."
    kill_process "vite"
    ;;
  *)
    echo "🛑 Stopping both client + server..."
    kill_process "uvicorn"
    kill_process "vite"
    ;;
esac
