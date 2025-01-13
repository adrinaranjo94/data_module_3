import asyncio
import websockets

connected_clients = set()

async def handler(websocket, path):
    # Añadir nuevo cliente
    connected_clients.add(websocket)
    print(f"Nuevo cliente conectado: {websocket.remote_address}")
    try:
        # Escuchar mensajes entrantes de este cliente
        async for message in websocket:
            print(f"Mensaje recibido de {websocket.remote_address}: {message}")
            # Reenviar el mensaje a los demás clientes conectados
            for client in connected_clients:
                if client != websocket:
                    await client.send(f"({websocket.remote_address}) dice: {message}")
    except websockets.ConnectionClosed:
        print(f"Cliente desconectado: {websocket.remote_address}")
    finally:
        # Eliminar el cliente al desconectarse
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Servidor WebSocket escuchando en ws://localhost:8765")
        # Mantener el servidor funcionando
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
