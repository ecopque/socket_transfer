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
        # Receive the file name: #3:
        file_name = receive_message(sock)
        if not file_name:
            return False
        
        # Create the 'file/' folder if it does not exist: #4:
        os.makedirs('file', exist_ok=True)

        # Path of the file where it will be saved: #5:
        file_path = os.path.join('file', file_name)

        # Open the file for binary writing: #6:
        with open(file_path, 'wb') as file:
            while True:
                file_data = sock.recv(1024)
                if not file_data:
                    break
                file.write(file_data)
        
        print(f'File {file_name} received successfully.')

        # Send confirmation AFTER the file has been written
        sock.send(b'File received successfully.')
        return True
    
    except Exception as error:
        print(f'Error: {error}')

# Server configuration: #7:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(50)

print('Server running...')

# Main listening loop: #8:
while True:
    try:
        newSock, _ = sock.accept()
        print('Received connection.')

        # Receive and print the message: #9:
        message = receive_message(newSock)
        if message:
            print(f'Received message: {message}')
            newSock.send(b'Message received successfully-1.')
        
        # Receive the file: #10:
        if receive_file(newSock, 'file'):
            print('File received successfully (confirmed).')
            newSock.send(b'File received successfully.')
        newSock.close()

    except Exception as error:
        print(f'Error: {error}')

# Need close connection?