# FILE: /client.py

import socket
import os

HOST = 'localhost'
PORT = 8002

# Function to send message:
def send_message(sock, message):
    try:
        sock.send(message.encode())

        # Waiting for server response:
        confirmation = sock.recv(1024).decode()
        print(f'Server: {confirmation}')

    except Exception as error:
        print(f"Error sending message: {error}")

# Function to send files:
def send_file(sock, file_path):
    try:
        # Get the file name and send it first:
        file_name = os.path.basename(file_path)
        send_message(sock, file_name)

        # Send the contents of the file:
        with open(file_path, 'rb') as file:
            sock.send(file.read())

            # Wait for server response about file:
            confirmation = sock.recv(1024).decode()
            print(f'Server: {confirmation}')

    except Exception as error:
        print(f"Error sending file: {error}")

# Client configuration:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Send a message to the server:
send_message(sock, 'Client running...')

# Upload a file to the server:
send_file(sock, 'image.png')

# Close the connection:
sock.close()