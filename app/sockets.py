from flask_socketio import emit
from app import socketio


@socketio.on("connect")
def on_connect():
    emit("server_message", {"msg": "Connected to live task feed"})


def broadcast_task_event(event: str, payload: dict) -> None:
    """Broadcast a task lifecycle event to all clients."""
    socketio.emit(event, payload)
