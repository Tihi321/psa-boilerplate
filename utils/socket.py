import eventlet
import socketio
from eventlet import wsgi

sio = socketio.Server(
    cors_allowed_origins='*',
    async_mode='eventlet',
    async_handlers=True,
    logger=True,
    engineio_logger=True
)
app = socketio.WSGIApp(sio)

def get_socket_server():
    return sio

def get_socket_app():
    return app

def run_server():
    """Run the Socket.IO server"""
    wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app, log_output=True)
