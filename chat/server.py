import socket   # socket module must be imported

host = "127.0.0.1"    # This is to create socket so that it can be bind with an ip and port number.
port = 3001           # This is to create socket.
CHUNK = 65535         # How much bytes server can receive at a time

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # This is to create socket object. \
                                                                # (defines ipv4, defines UDP)
socket_obj.bind((host, port))                                   # socket object binds the host and port to create socket

while True:
    data, client_addr = socket_obj.recvfrom(CHUNK)  # recvfrom function is used to get data (in bytes) and socket of client.
    message = data.decode('ascii')                  # We have to decode data to present in ascii form
    print(f"client: {message}")                     # Finally this statement print data on screen.
    message_send = input("Reply: ")                 # Server wants to send data and type the message
    data = message_send.encode('ascii')             # Server will have to encode data before sending
    socket_obj.sendto(data, client_addr)            # Finally server send data to the client socket(IP + port)
