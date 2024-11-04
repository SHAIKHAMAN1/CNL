import socket
import os

host = "127.0.0.1"
port = 12000
buffer_size = 1024
file_name = 'C:\\Users\\amaan\\OneDrive\\Desktop\\CN\\Myfile2.txt'  # Use double backslashes

# Alternatively, you can use forward slashes
# file_name = 'C:/Users/amaan/OneDrive/Desktop/CN/Myfile.txt'

# Check if file exists before proceeding
if not os.path.isfile(file_name):
    print(f"Error: {file_name} not found!")
else:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with open(file_name, "r") as f:
        data = f.read(buffer_size)
        while data:
            print(data)
            if sock.sendto(data.encode(), (host, port)):
                data = f.read(buffer_size)
        sock.sendto("Now".encode(), (host, port))
    sock.close()
