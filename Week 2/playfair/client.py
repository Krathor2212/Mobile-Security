import socket
from playfair import encrypt,decrypt
host='127.0.0.1'
port = 5004
client = socket.socket()
client.connect((host,port))
message = ''

while message != 'q':
    message = input("Enter Client Message: ")
    if message == 'q':
        break
    key = input("Enter the Key: ")
    print(f'Client: {message}')


    encrypt_message = encrypt(message,key)
    message = f'{encrypt_message}:{key}'
    client.send(message.encode())

    message = client.recv(1024).decode()
    print("Encrypted Message from Server: "+ message)

    t = message.split(':')
    message,key = t[0],t[1]
    decrypt_message = decrypt(message,key)
    print(f'Server: {decrypt_message}')

    if message == 'q':
        break
client.close()