import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 3334         # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))   # Bind the socket to the address and port
    s.listen()             # Listen for incoming connections
    print(f"Server listening on {HOST}:{PORT}...")
    
    conn, addr = s.accept()  # Accept connection from client
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode()  # Receive data from the client
            print('Client says:', data)
            if data == 'stop':  # Stop the conversation
                break
            response = input("Enter your message: ")
            conn.sendall(response.encode())  # Send message back to the client
