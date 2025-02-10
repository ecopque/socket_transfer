#server

# import socket
# import os

# HOST = 'localhost'
# PORT = 8002

# def receive_message(sock, buffer_size=1024):
#     try:
#         message = sock.recv(buffer_size)
#         return message

#     except Exception as error:
#         print(f'Error: {error}')
#         return None

# def receive_file(sock, file_path):
#     try:
#         file_name = receive_message(sock)
#         if not file_name:
#             return False

#         os.makedirs('file', exist_ok=True)
#         file_path = os.path.join('file', file_name)

#         with open(file_path, 'wb') as file:
#             while True:
#                 file_data = sock.recv(1024)
#                 if not file_data:
#                     break
#                 file.write(file_data)
        
#         print(f'File {file_name} received successfully.')
#         sock.send('File received successfully.')
#         return True
    
#     except Exception as error:
#         print(f'Error: {error}')

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(HOST, PORT)
# sock.listen(5)

# print('Server running...')

# while True:
#     try:
#         newSock, _ = sock.accept()
#         print('Received connection...')

#         message = receive_message(newSock)
#         if message:
#             print(f'Received message: {message}')
#             newSock.send(b'Received message.')

#         if receive_file(newSock, 'file/'):
#             print(f'File received.')
#             newSock.send(b'Received file.')
#         newSock.close()

#     except Exception as error:
#         print(f'Error: {error}')

# client

import socket
import os

HOST = 'localhost'
PORT = 8002

def send_message(sock, message):
    try:
        sock.send(message.encode())
        confirmation = sock.recv(1024).decode()
        print(f'Server: {confirmation}')
    
    except Exception as error:
        print(f'Error: {error}')


def send_file(sock, file_path):
    try:
        file_name = os.path.basename(file_path)
        send_message(sock, file_name)

        with open(file_path, 'rb') as file:
            sock.send(file.read())

            confirmation = sock.recv(1024).decode()
            print(f'Server: {confirmation}')

    except Exception as error:
        print(f'Error: {error}')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST, PORT)
sock.listen(5)

send_message(sock, 'Foi...')
send_file(sock, 'image.png')
sock.close()