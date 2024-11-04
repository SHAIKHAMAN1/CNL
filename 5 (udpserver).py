import socket

# Server information
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

# Message to send to the client
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

# Create a UDP socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and port
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = f"Message from Client: {message}"
    clientIP = f"Client IP Address: {address}"
    print(clientMsg)
    print(clientIP)

    # Send a reply to the client
    UDPServerSocket.sendto(bytesToSend, address)
