import socket
import os

HOST = 'localhost'
PORT = 8002

# Receber mensagem:
def receive_message(sock, buffer_size=1024):
    try:
        message = sock.recv(buffer_size).decode()
        return message
    
    except Exception as error:
        print(f'Error: {error}')
        return None
    
# Receber arquivo:
def receive_file(sock, file_path):
    try:
        file_name = receive_message(sock)
        if not file_name:
            return False

        # Crie o arquivi/pasta se não existir:
        file_path = os.path.join('file', file_name)

        # Abra o arquivo em modo de escrita em binário:
        with open(file_path, 'wb') as file:
            file_data = sock.recv(1024)
            if not file_data:
                break
            file.write(file_data)

        print(f'File {file_name} received successfully.')
        return True
    except Exception as error:
        print(f'Error: {error}')

# Criando a conexão:
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

print(f'Server running...')

# A hora do show:
while True:
    try:
        newSock, _ = sock.accept()
        print('Received connection.')

        message = receive_message(newSock)
        if message:
            print(f'Received message {message}')
            newSock.send(b'Received message, client.')

        if receive_file(newSock, 'file/'):
            print(f'Received file.')
            newSock.send(b'Received file.')
        newSock.close()

    ...