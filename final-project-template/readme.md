# Práctica IoT & Big Data con Docker Compose

Este proyecto demuestra cómo integrar:

- **Mosquitto** (broker MQTT)
- **ThingsBoard** (plataforma IoT con dashboards y rule engine)
- **Kafka** + **Zookeeper** (streaming distribuido)
- Un contenedor adicional que simula un **publicador MQTT** (`mqtt-publisher`)

## Estructura

- `docker-compose.yml`: Arranca todos los contenedores necesarios.
- `mosquitto/mosquitto.conf`: Configuración básica para Mosquitto.
- `scripts/kafka_consumer.sh`: Script de ejemplo para consumir datos de un topic de Kafka.
- `scripts/mqtt_sub.sh`: Script para suscribirse a un topic MQTT (opcional, si tienes mosquitto clients en el host).

## Requisitos

- Docker y Docker Compose instalados.
- Puertos libres: 1883 (MQTT), 8080 (ThingsBoard), 9092 (Kafka), 2181 (Zookeeper), etc.

## Pasos para la Práctica

1. **Clona** este repositorio y navega hasta la carpeta `practica_iot_bigdata`.
2. Ajusta configuraciones si lo deseas (credenciales, nombres de contenedor, etc.).
3. Ejecuta `docker-compose up -d` para levantar todos los contenedores.
4. Espera unos segundos y verifica que todos estén corriendo con `docker ps`.

### Verificar Publicación en Mosquitto

- El contenedor `mqtt-publisher` envía datos cada pocos segundos al topic `sensors/temperature`.
- Para comprobarlo, usa un cliente MQTT local o el script `mqtt_sub.sh` (si lo deseas).

### Acceder a ThingsBoard

- Abre [http://localhost:8080](http://localhost:8080) en tu navegador.
- Usuario/Contraseña por defecto (si no lo has cambiado) suele ser `tenant@thingsboard.org` / `tenant`.
- Configura un **Device** y un **Data Connector** para suscribirte al topic `sensors/temperature`.
- Crea un **Dashboard** básico para visualizar los valores recibidos.

### Forward a Kafka (Opcional)

- En la configuración de ThingsBoard o a través de su Rule Engine, reenvía los datos al broker Kafka (`kafka:9092`).
- Usa `scripts/kafka_consumer.sh` para verificar que los mensajes llegan al topic correspondiente.

### Limpieza

- Para bajar todos los contenedores, ejecuta `docker-compose down`.
- Si deseas eliminar volúmenes o datos persistidos, añade la opción `-v`: `docker-compose down -v`.

¡Listo! Con esto, demuestras cómo integrar el ecosistema IoT/Big Data con Docker Compose de forma sencilla.
