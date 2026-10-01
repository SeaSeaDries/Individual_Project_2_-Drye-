def encrypt(message, n):
    final = [] 
    count = 1

    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            pos = (ord(char) - start + (count * n)) % 26

            final.append(chr(start + pos))

            count += 1 
        else:
            final.append(char)
        
    return "".join(final)

def decrypt(message, n):
    pass