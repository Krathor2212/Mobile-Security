def mod_inv(v,m):
    for i in range(1,m):
        if (v*i) % m ==1:
            return i
    raise ValueError(f"Inverse of {v} mod {m} does not exist")

def encrypt(key,text):
    if key % 2 == 0 or key %13 == 0:
        raise ValueError("Key is not valid")
    ct = ""
    for i in text:
        if "a" <= i <="z":
            t = ord(i) - ord('a')
            t = (t*key)%26
            ct += chr(t+ord('a'))
        elif "A" <= i <="Z":
            t = ord(i) - ord('A')
            t = (t*key)%26
            ct += chr(t+ord('A'))    
        else:
            ct += i
    return ct

def decrypt(key,text):
    inv_key = mod_inv(key,26)
    pt = ""
    for i in text:
        if "a" <= i <= "z":
            t = ord(i) - ord('a')
            t = (t*inv_key)%26
            pt += chr(t+ord('a'))
        elif "A" <= i <= "Z":
            t = ord(i) - ord('A')
            t = (t*inv_key)%26
            pt += chr(t+ord('A'))
        else:
            pt += i
    return pt


