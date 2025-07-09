import socket
from multi_cryptors import encrypt,decrypt
host = "127.0.0.1"
port = 5001
key = 3
server = socket.socket()
server.bind((host,port))
server.listen()
while True:
    conn,addr = server.accept()
    print("Request Accepted from "+ str(addr))
    message = conn.recv(1024).decode()
    if not message:
        response = "Something went Wrong"
    else:
        message = decrypt(key,message)
        print("Decrypted Message: "+message)
        try:
            username,password = message.split(":")
            if username == "admin" and password == "purush":
                 response = "Successfull Login"
            else:
                response = "Invalid Credentials"
        except ValueError:
            response = "Message not in the expected Format"
    response = encrypt(key,response)
    conn.send(response.encode())
    conn.close()