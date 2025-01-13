import asyncio
import websockets

async def listen_messages(websocket):
    """
    Tarea asíncrona que escucha mensajes provenientes del servidor
    y los imprime en pantalla.
    """
    try:
        async for message in websocket:
            print(f"[Mensaje del servidor] {message}")
    except websockets.ConnectionClosed:
        print("Conexión cerrada con el servidor.")

async def main():
    uri = "ws://localhost:8765"
    print(f"Intentando conectar con el servidor en {uri}...")
    
    # Conectarse al servidor
    async with websockets.connect(uri) as websocket:
        print("Conectado al servidor WebSocket.")

        # Iniciar la tarea de escucha en segundo plano
        listen_task = asyncio.create_task(listen_messages(websocket))

        # Bucle para enviar mensajes
        while True:
            mensaje = input("Escribe un mensaje (o 'exit' para salir): ")
            if mensaje.lower() == "exit":
                print("Cerrando conexión...")
                break
            # Enviar el mensaje al servidor
            await websocket.send(mensaje)

        # Cancelar la tarea de escucha
        listen_task.cancel()
        print("Cliente finalizado.")

if __name__ == "__main__":
    asyncio.run(main())
