#!/bin/bash

PORT=$1

if [ -z "$PORT" ]; then
  echo "Usage: $0 <port>"
  exit 1
fi

echo "Searching for process listening on port $PORT..."

if command -v lsof &> /dev/null; then
  echo "[Using lsof]"
  sudo lsof -nP -iTCP:$PORT -sTCP:LISTEN
elif command -v ss &> /dev/null; then
  echo "[Using ss]"
  sudo ss -tulpn | grep ":$PORT"
elif command -v netstat &> /dev/null; then
  echo "[Using netstat]"
  sudo netstat -tulpn | grep ":$PORT"
else
  echo "No suitable tool found (lsof, ss, netstat)"
  exit 2
fi

