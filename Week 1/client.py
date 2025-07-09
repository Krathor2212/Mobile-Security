import socket
from multi_cryptors import encrypt,decrypt
host = "127.0.0.1"
port = 5001
key = 3
client = socket.socket()
client.connect((host,port))
username = input("Enter the Username: ")
password = input("Enter the Password: ")
message = encrypt(key,f"{username}:{password}")
print(message)
client.send(message.encode())
data = client.recv(1024).decode()
print("Server Message: "+ decrypt(key,str(data)))
client.close()