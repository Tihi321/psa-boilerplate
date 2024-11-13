import asyncio
import websockets
import json

connected_clients = set()

async def handle_client(websocket):
    """Handle individual client connections"""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            try:
                data = json.loads(message)
                # Handle the message and send response
                response = {'type': 'message', 'data': f'Server received: {data}'}
                await websocket.send(json.dumps(response))
            except json.JSONDecodeError:
                print(f"Invalid JSON received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Client connection closed")
    finally:
        connected_clients.remove(websocket)

async def websocket_server():
    """Create and run the WebSocket server"""
    async with websockets.serve(handle_client, "127.0.0.1", 5000):
        await asyncio.Future()  # run forever

def run_server():
    """Run the WebSocket server in a separate thread"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(websocket_server())

def broadcast_message(message):
    """Broadcast a message to all connected clients"""
    websockets.broadcast(connected_clients, json.dumps(message))
