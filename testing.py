import socket
import os

HOST = 'localhost'
PORT = 8002

def receive_message(sock, buffer_size=1024):
    try:
        message = sock.recv(buffer_size)
        return message

    except Exception as error:
        print(f'Error: {error}')
        return None

def receive_file(sock, file_path):
    try:
        file_name = receive_message(sock)
        if not file_name:
            return False

        os.makedirs('file', exist_ok=True)
        file_path = os.path.join('file', file_name)