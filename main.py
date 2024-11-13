from threading import Thread
from config import DEV_URL, FRONTEND_DIST_FILE, WINDOW_TITLE
import argparse
import os
from backend.Main import Main
import utils.assets as assets
import utils.socket as socket
import utils.window as window

backend = Main()

def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument('--dev', action='store_true', help='Run in development mode')

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
