import socket

# Message to send to the server
msgFromClient = "Hello UDP Server"
bytesToSend = str.encode(msgFromClient)

# Server information
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Create a UDP socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send the message to the server
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# Receive a reply from the server
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

# Print the server's reply
msg = f"Message from Server: {msgFromServer[0].decode()}"
print(msg)
