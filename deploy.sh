#!/bin/bash

command -v docker >/dev/null || { echo "Docker missing"; exit 1; }
command -v docker-compose >/dev/null || { echo "Compose missing"; exit 1; }

docker-compose down -v
docker-compose up --build -d

echo "[SUCCESS] Application is live at http://localhost"
