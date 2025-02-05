import socket
import os

HOST = 'localhost'
PORT = 8002

def receive_message(sock, buffer_size=1024):
    try:
        message = sock.recv(buffer_size).decode()
        return message
    except Exception as error:
        print(f'Error: {error}')
        return None
    