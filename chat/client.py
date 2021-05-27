import socket   # socket module must be imported

port = 3001     # This is to create socket.
host = "127.0.0.1"  # This is to create socket so that it can be bind with an ip and port number.
CHUNK = 65535       # How much bytes server can receive at a time

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # This is to create socket object. \
                                                                # (defines ipv4, defines UDP)

while True:
    socket_obj.connect((host, port))      # Connect func is used to connect socket to the defined host and port(server)
    message = input("Type message: ")     # Client will send the msg first.
    data = message.encode('ascii')        # Data must be encoded before sending to client.
    socket_obj.send(data)                 # send func is used to send data to connected socket
    data = socket_obj.recv(CHUNK)         # recv func will get data whatever will server send, in bytes
    text = data.decode('ascii')           # data must be decoded before showing up on screen.
    print(f"Server says: {text}")         # finally server data is printed.
