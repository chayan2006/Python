# 🌐 Networking in Python: Low-level Sockets

import socket

# 1. Simple Server (TCP)
# Run this in one terminal...
# (Already exists here for your notes, but uncomment to test)
'''
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server.bind(("127.0.0.1", 9999))
    server.listen(1)
    print("Server is listening on 127.0.0.1:9999...")
    
    client, addr = server.accept()
    print(f"Connected to {addr}")
    
    msg = client.recv(1024).decode("utf-8")
    print(f"Received from client: {msg}")
    
    client.send("Hello from Server!".encode("utf-8"))
    client.close()
'''

# 2. Simple Client (TCP)
# ...Run this in another terminal
'''
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    
    client.send("Hello from Client!".encode("utf-8"))
    msg = client.recv(1024).decode("utf-8")
    print(f"Received from server: {msg}")
    
    client.close()
'''

# 3. Getting your own IP / Hostname
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

# Summary Table
"""
| Method            | Purpose                                        |
|-------------------|------------------------------------------------|
| socket.socket()   | Create a new socket object                     |
| .bind(addr)       | Associate socket with an IP/Port               |
| .listen()         | Start listening for incoming connections       |
| .accept()         | Accept a new connection (Blocks until one comes)|
| .connect(addr)    | Connect to a remote server                     |
| .send() / .recv() | Send and Receive data across network           |
| .close()          | Shut down the connection                       |
"""
