import socket

# Define our host and port
HOST, PORT = "localhost", 8888

# Create our socket for connections (Internet Socket, TCP Protocol)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to our host and port
socket.bind((HOST, PORT))

# If more than a specified number of connections are "waiting"
# in this case 5, block extra incoming connections.
socket.listen(5)

print(f"Server started on port {PORT}!")

# Listen for connections
while True:
    # Receive client connections
    client_socket, client_addr = socket.accept()
    print(f"Connected to {client_addr}!")

    # Client will send information
    client_message = client_socket.recv(1024).decode("utf-8")
    print(f"Message from client: {client_message}")

    # Server response
    server_response = "Thank you for your message!"

    # Server response must be encoded
    server_response.encode("utf-8")

    # Send the server response
    client_socket.send(server_response)

    # Terminate the connection
    client_socket.close()
    print(f"Connection with {client_addr} terminated!")
