import socket
import os

# Create UDP client
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)

# Use raw string to handle backslashes correctly
file_path = r"C:\Users\amaan\OneDrive\Desktop\CN\sample.mp4"  # Or use raw string notation
# Alternatively, you can use double backslashes
# file_path = "C:\\Users\\amaan\\OneDrive\\Desktop\\CN\\new.txt"
# Or use forward slashes
# file_path = "C:/Users/amaan/OneDrive/Desktop/CN/new.txt"

# Check if the provided file path is valid
if not os.path.isfile(file_path):
    print(f"Error: {file_path} not found!")
else:
    file_extension = file_path.split('.')[-1]

    try:
        # Notify server of the file type
        udp_client.sendto(f'FILETYPE:{file_extension}'.encode('utf-8'), server_address)

        # Read the file in chunks and send over UDP
        with open(file_path, 'rb') as f:
            chunk = f.read(4096)
            while chunk:
                udp_client.sendto(chunk, server_address)
                chunk = f.read(4096)
        udp_client.sendto(b'EOF', server_address)
        print("File sent successfully.")

        # Wait for the acknowledgment from the server
        udp_client.settimeout(5)
        try:
            ack, server = udp_client.recvfrom(4096)
            if ack == b'ACK':
                print("Server acknowledged the receipt of the file.")
        except socket.timeout:
            print("No acknowledgment received from the server.")
    finally:
        udp_client.close()
