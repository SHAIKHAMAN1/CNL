import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 3334         # The port used by the server

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    while True:
        message = input("Enter your message: ")
        s.sendall(message.encode())  # Send message to the server
        if message == 'stop':  # Stop the conversation
            break
        data = s.recv(1024).decode()  # Receive response from the server
        print('Server says:', data)
