import string

def generate_key_matrix(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    key_string = ""
    for char in key:
        if char in string.ascii_uppercase and char not in seen:
            seen.add(char)
            key_string += char
    # Add remaining letters (excluding J)
    for char in string.ascii_uppercase:
        if char == 'J':
            continue
        if char not in seen:
            key_string += char

    # Create 5x5 matrix
    matrix = [list(key_string[i*5:(i+1)*5]) for i in range(5)]
    return matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def prepare_text(text, for_encryption=True):
    text = text.upper().replace('J', 'I')
    filtered = [c for c in text if c in string.ascii_uppercase]
    if not for_encryption:
        return filtered

    # Insert 'X' between duplicate letters in pairs
    i = 0
    result = []
    while i < len(filtered):
        result.append(filtered[i])
        if i+1 < len(filtered):
            if filtered[i] == filtered[i+1]:
                result.append('X')
                i += 1
            else:
                result.append(filtered[i+1])
                i += 2
        else:
            i += 1
    if len(result) % 2 != 0:
        result.append('X')
    return result

def encrypt(plaintext, key):
    matrix = generate_key_matrix(key)
    prepared = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            ciphertext += matrix[r1][(c1+1)%5]
            ciphertext += matrix[r2][(c2+1)%5]
        elif c1 == c2:
            ciphertext += matrix[(r1+1)%5][c1]
            ciphertext += matrix[(r2+1)%5][c2]
        else:
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]
    return ciphertext

def decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)
    prepared = prepare_text(ciphertext, for_encryption=False)
    plaintext = ""

    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:
            plaintext += matrix[r1][(c1-1)%5]
            plaintext += matrix[r2][(c2-1)%5]
        elif c1 == c2:
            plaintext += matrix[(r1-1)%5][c1]
            plaintext += matrix[(r2-1)%5][c2]
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]
    return plaintext
