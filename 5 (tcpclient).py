import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9999

# Connect to the server
s.connect((host, port))

# Receive data from the server
hello_message = s.recv(1024)
s.close()

# Print the received message from the server
print(f"Message from the server: {hello_message.decode('ascii')}")
