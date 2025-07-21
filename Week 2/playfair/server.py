import socket
from playfair import encrypt,decrypt
host = '127.0.0.1'
port = 5004
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
        t = message.split(':')
        message,key = t[0],t[1]
        decrypt_message = decrypt(message,key)
        print(f'Client: {decrypt_message}')

        if message == 'q':
            break

        message = input("Enter Server Message: ")
        if message == 'q':
            break
        key = input("Enter Server Key: ")
        print(f'Server : {message}')
        

        encrypt_message = encrypt(message,key)
        tosend_message = f'{encrypt_message}:{key}'
        conn.send(tosend_message.encode())
        
conn.close()
    