import socket

# Define server address and port
host = "127.0.0.1"
port = 12000

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

# Open a file to write the incoming data
with open('Myfile2.txt', 'wb') as f:
    print('New file created, waiting for data...')

    while True:
        data, addr = sock.recvfrom(1024)  # Receive data in chunks of 1024 bytes
        if data.decode("utf-8") == "Now":  # End signal from client
            break
        f.write(data)  # Write the received data into the file

    print('File is successfully received!')

# Open and display the content of the file
with open('Myfile2.txt', 'r') as f:
    print(f.read())

sock.close()
print('Connection closed!')
