import socket
import time
import subprocess

# Create UDP server
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 8080))
print("UDP server listening for file...")

file_types = {
    'mp4': 'C:\\Users\\amaan\\OneDrive\\Desktop\\CN\\received_file.mp4',
    'txt': 'C:\\Users\\amaan\\OneDrive\\Desktop\\CN\\received_file.txt',
    'py': 'C:\\Users\\amaan\\OneDrive\\Desktop\\CN\\received_file.py',
    'mp3': 'C:\\Users\\amaan\\OneDrive\\Desktop\\CN\\received_file.mp3'
}
file_type = None
f = None

try:
    while True:
        data, client_address = udp_server.recvfrom(4096)
        if data.startswith(b'FILETYPE:'):
            file_extension = data.split(b':')[1].decode('utf-8').strip()
            if file_extension in file_types:
                file_type = file_extension
                f = open(file_types[file_type], 'wb')
            continue
        elif data == b'EOF':
            break
        if f:
            f.write(data)
    if f:
        f.close()
    print("File received successfully.")
finally:
    udp_server.close()

# Wait for 5 seconds before playing the file (optional, remove if not needed)
time.sleep(5)

# Play the received file using Windows Media Player if it's a video or audio file
if file_type in ['mp4', 'mp3']:
    file_path = file_types[file_type]
    subprocess.run(['start', 'wmplayer', file_path], shell=True)
