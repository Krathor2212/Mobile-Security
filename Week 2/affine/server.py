import socket
from affine import encrypt,decrypt
host = '127.0.0.1'
port = 5003
a,b = 3,9
server = socket.socket()
server.bind((host,port))
server.listen()
message = ''
conn,addr = server.accept()
print("Request accepted from "+str(addr))
while message != 'q':
    message = conn.recv(1024).decode()
    if not message:
        break
    else:
        message = decrypt(a,b,message)
        print(f'CLient: {message}')
        if message == 'q':
            break
        message = input("Enter Server Message: ")
        print(f'Server : {message}')
        message = encrypt(a,b,message)
        conn.send(message.encode())
        if message == 'q':
            break
conn.close()
    