# **Socket File Transfer**

This project implements a **simple file transfer system** using **Python 3.11 and TCP sockets**. It allows a client to send messages and files to a server, which receives and stores them in a designated directory.

---

## **Technologies Used**
- **Python 3.11** – The primary programming language.
- **Sockets** – Used for communication between the client and server over TCP.
- **OS Module** – Handles file operations such as saving received files.

---

## **Project Structure**
- socket-file-transfer
- file/ # Directory where received files are stored
- server.py # Server script (receives messages and files)
- client.py # Client script (sends messages and files) 
- README.md # Project documentation

- **server.py**:
  - Listens for incoming connections on **port 8002**.
  - Receives and prints messages sent by the client.
  - Receives files and stores them in the **file/** directory.
  - Sends confirmation messages to the client.

- **client.py**:
  - Connects to the server on **port 8002**.
  - Sends a text message to the server.
  - Sends a file (`image.png`) to the server.
  - Receives confirmation messages from the server.

---

## **Setup and Execution**
### ** Clone the repository**
```bash
git clone https://github.com/your-username/socket-file-transfer.git
cd socket-file-transfer
```