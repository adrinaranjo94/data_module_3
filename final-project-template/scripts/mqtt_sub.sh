#!/usr/bin/env bash
# 
# Script para suscribirse a un topic MQTT en localhost:1883
# Necesitas tener instalado 'mosquitto-clients' localmente.

TOPIC=${1:-"sensors/temperature"}

echo "Suscribiéndose al topic: $TOPIC (localmente)"
mosquitto_sub -h localhost -p 1883 -t "$TOPIC"
