def encrypt(a,b,pt):
    ct = ''
    if a%2 == 0 or a%13 == 0 or b%2==0 or b%13==0:
        raise ValueError(f"Given {a} and {b} are not coprime with 26")
    for i in pt:
        if ord('a') <= ord(i) <= ord('z'):
            x = ord(i)-ord('a')
            t = (a*x+b)%26
            ct += chr(t+ord('a'))
        elif ord('A') <= ord(i) <= ord('Z'):
            x = ord(i)-ord('A')
            t = (a*x+b)%26
            ct += chr(t+ord('Z'))
        else:
            ct += i
    return ct

def mod_inv(v,m):
    for i in range(m):
        if (v*i) % m == 1:
            return i
    raise ValueError(f"Couldnt find the mod inv for {v}")

def decrypt(a,b,ct):
    pt = ''
    a_inv = mod_inv(a,26)
    for i in ct:
        if ord('a') <= ord(i) <= ord('z'):
            y = ord(i)-ord('a')
            t = a_inv*(y-b)%26
            pt += chr(t+ord('a'))
        elif ord('A') <= ord(i) <= ord('Z'):
            y = ord(i)-ord('A')
            t = a_inv*(y-b)%26
            pt += chr(t+ord('Z'))
        else:
            pt += i
    return pt
