import webview
import os
from threading import Thread
from backend.Main import Main
import utils.assets as assets
import utils.socket as socket

backend = Main()
sio = socket.get_socket_server()

# Socket.IO event handlers
@sio.event
def connect(sid, environ):
    print(f'Client connected: {sid}')
    sio.emit('message', backend.greet())

@sio.event
def disconnect(sid):
    print(f'Client disconnected: {sid}')

@sio.event
def message(sid, data):
    print(f'Message received: {data}')
    socket.sio.emit('message', f'Server received: {data}')

def main():
    # Start Socket.IO server in a separate thread
    server_thread = Thread(target=socket.run_server, daemon=True)
    server_thread.start()

    # In development, use Vite's dev server
    if os.environ.get('DEV'):
        url = "http://localhost:3000"
    else:
        # In production, use the built files
        url = assets.get_asset_path(os.path.join('frontend', 'dist', 'index.html'))

    # Create and start webview window
    webview.create_window('Solid + Python WebView', url, width=800, height=600)
    webview.start(debug=True)


if __name__ == '__main__':
    main()
