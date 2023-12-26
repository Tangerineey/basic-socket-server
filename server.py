import socket

# Define our host and port
HOST, PORT = "localhost", 8888

# Create our socket for connections (Internet Socket, TCP Protocol)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to our host and port
server_socket.bind((HOST, PORT))

# If more than a specified number of connections are "waiting"
# in this case 5, block extra incoming connections.
server_socket.listen(5)

print(f"Server started on port {PORT}!")

# Listen for connections
while True:
    # Receive client connections
    client_socket, client_addr = server_socket.accept()
    print(f"Connected to {client_addr}!")

    # Client will send information
    client_message = client_socket.recv(1024).decode(
        "utf-8"
    )  # 1024 is the max byte size for responses
    print(f"Message from client: {client_message}")

    # Server response, and it must be encoded
    server_response = "Thank you for your message!".encode("utf-8")

    # Send the server response
    client_socket.send(server_response)

    # Terminate the connection
    client_socket.close()
    print(f"Connection with {client_addr} terminated!")
