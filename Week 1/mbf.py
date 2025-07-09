import socket
from multi_cryptors import encrypt,decrypt

host = "127.0.0.1"
port = 5001

leaked = input("Enter the leaked message: ")

for i in range(26):
    if i % 2 != 0 and i % 13 != 0:
        guessed_key = i 
        decrypted = decrypt(i,leaked)
        print(f"key: {i}\nMessage: {decrypted}")
        attacker = socket.socket()
        try:
            attacker.connect((host,port))
            guessed_key_encrypted = encrypt(i,decrypted)
            attacker.send(guessed_key_encrypted.encode())

            message = decrypt(i,attacker.recv(1024).decode())
            if message == "Successfull Login":
                print(f"Crt Key is {i}\n")
                break
            else:
                print(f"{i} is not the crt key")
        except Exception:
            print("something went wrong")
        finally:
            attacker.close()
else:
    print("Brute Force Failed")
