
#!/usr/bin/env bash
# 
# Script que ingresa al contenedor Kafka y lanza un consumer
# Ejemplo de uso: ./kafka_consumer.sh <nombre_topic>

TOPIC=${1:-"tb_rule_engine.topic"}  # Por defecto, usa 'tb_rule_engine.topic' si no pasas argumento

echo "Iniciando consumer para el topic: $TOPIC"
docker exec -it kafka bash -c "
  kafka-console-consumer.sh \
    --bootstrap-server localhost:9092 \
    --topic $TOPIC \
    --from-beginning
"
