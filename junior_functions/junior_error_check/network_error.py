import socket

def network_status():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError as err: pass  # Use it for logs.
    return False
