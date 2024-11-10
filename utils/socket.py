import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)

def get_socket_server():
    return sio

def get_socket_app():
    return app

def run_server():
    """Run the Socket.IO server"""
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)