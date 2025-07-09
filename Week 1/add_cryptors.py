def encrypt(key,text):
    ct = ""
    for i in text:
        if "a" <= i <="z":
            t = ord(i) - ord('a')
            t = (t+key)%26
            ct += chr(t+ord('a'))
        elif "A" <= i <="Z":
            t = ord(i) - ord('A')
            t = (t+key)%26
            ct += chr(t+ord('A'))    
        else:
            ct += i
    return ct

def decrypt(key,text):
    pt = ""
    for i in text:
        if "a" <= i <= "z":
            t = ord(i) - ord('a')
            t = (t-key)%26
            pt += chr(t+ord('a'))
        elif "A" <= i <= "Z":
            t = ord(i) - ord('A')
            t = (t-key)%26
            pt += chr(t+ord('A'))
        else:
            pt += i
    return pt


