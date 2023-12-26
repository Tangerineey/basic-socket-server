import socket

# The address of the server
SERVER_ADDR, SERVER_PORT = "localhost", 8888

# Create our client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Using our client socket, connect to the server
client_socket.connect((SERVER_ADDR, SERVER_PORT))

# Client will send message to server
client_message = "Hello Server!".encode("utf-8")
client_socket.send(client_message)

# Display any server responses
server_response = client_socket.recv(1024)
print(f"Server response = {server_response}")
