import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Bind to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

print("Server is listening...")

while True:
    # Establish a connection
    clientsocket, addr = serversocket.accept()
    print(f"Got a connection from {str(addr)}")

    # Send "Hello" message to the client
    hello_message = "Hello, client!" + "\r\n"
    clientsocket.send(hello_message.encode('ascii'))

    # Close the connection
    clientsocket.close()
