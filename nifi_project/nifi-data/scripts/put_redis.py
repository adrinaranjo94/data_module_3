import redis

# Configura la conexión a Redis
r = redis.StrictRedis(host='redis', port=6379, db=0)

# Obtén el contenido del FlowFile
flowfile_content = session.read(flowfile)
content = flowfile_content.decode('utf-8')  # Convierte el contenido a string

# Escribe en Redis (usa una clave personalizada)
r.set("my_key", content)

# Continúa el flujo
session.transfer(flowfile, REL_SUCCESS)
