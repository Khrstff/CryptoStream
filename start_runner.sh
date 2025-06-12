#!/bin/bash
echo "Iniciando runner cada 5 segundos..."

while true
do
    python3 runner.py
    sleep 5
done
