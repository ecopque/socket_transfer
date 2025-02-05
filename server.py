# FILE: /server.py

import socket
import os

HOST = 'localhost'
PORT = 8002

# Function to receive messages: #1:
def receive_message(sock, buffer_size=1024):
    try:
        message = sock.recv(buffer_size).decode()
        return message
    
    except Exception as error:
        print(f'Error: {error}')
        return None
    
# Function to receive files: #2:
def receive_file(sock, file_path):
    try:
        # Receive the file name:
        file_name = receive_message(sock)
        if not file_name:
            return False
        
        # Create the 'file/' folder if it does not exist:
        os.makedirs('file', exist_ok=True)

        # Path of the file where it will be saved:
        file_path = os.path.join('file', file_name)

        # Open the file for binary writing:
        with open(file_path, 'wb') as file:
            while True:
                file_data = sock.recv(1024)
                if not file_data:
                    break
                file.write(file_data)
        
        print(f'File {file_name} received successfully.')
        return True
    
    except Exception as error:
        print(f'Error: {error}')

# Server configuration: #4:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

print('Server running...')

# Main listening loop:
while True:
    try:
        newSock, _ = sock.accept()
        print('Received connection.')

        # Receive and print the message:
        message = receive_message(newSock)
        if message:
            print(f'Received message: {message}')
            newSock.send(b'Message received successfully.')
        
        # Receive the file:
        if receive_file(newSock, 'file/'):
            newSock.send(b'File received successfully.')
        newSock.close()

    except Exception as error:
        print(f'Error: {error}')