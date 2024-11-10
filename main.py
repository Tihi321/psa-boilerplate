from config import DEV_URL, FRONTEND_DIST_FILE, WINDOW_TITLE
import argparse
import os
from threading import Thread
from backend.Main import Main
import utils.assets as assets
import utils.socket as socket
import utils.window as window

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
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('--dev', action='store_true', help='Run in development mode')

    # Start Socket.IO server in a separate thread
    server_thread = Thread(target=socket.run_server, daemon=True)
    server_thread.start()
    
    args = parser.parse_args()
    isDev = args.dev
    
    if isDev:
        print("Running in development mode")
    else:
        print("Running in normal mode")

    url = DEV_URL if isDev else assets.get_asset_path(os.path.join(FRONTEND_DIST_FILE))
    window.create_window(WINDOW_TITLE, url, debug=isDev)


if __name__ == '__main__':
    main()
