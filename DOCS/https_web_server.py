import socket

HOST, PORT = '', 8888

LISTEN_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LISTEN_SOCKET.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
LISTEN_SOCKET.bind((HOST,PORT))
LISTEN_SOCKET.listen(1)
print(f"Serving HTTP on port {PORT}")

while True:
    client_connection, client_address = LISTEN_SOCKET.accept()
    request = client_CONNECTION.recv(1024)
    print(request.decode('utf-8', errors='replace'))

    http_response = """\
    HTTP/1.1 200 OK

   #WRITING GOES HERE
    """

    client_CONNECTION.sendall(http_response.encode())
    client_CONNECTION.close()


