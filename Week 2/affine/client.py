import socket
from affine import encrypt,decrypt
host='127.0.0.1'
port = 5003
a,b = 3,9
client = socket.socket()
client.connect((host,port))
message = ''

while message != 'q':
    message = input("Enter Client Message: ")
    print(f'Client: {message}')
    if message == 'q':
        break
    client.send(encrypt(a,b,message).encode())
    message = client.recv(1024).decode()
    message = decrypt(a,b,message)
    print(f'Server: {message}')
    if message == 'q':
        break
client.close()