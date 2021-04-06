def caesarCipherEncryptor(string, key):
    # Write your code here.
    key = keySimplifier(key)
    return ''.join([chr(ord(ch) + key) if (ord(ch) + key) <= 122 else chr(96 + ord(ch) + key - 122) for ch in string])

def keySimplifier(key):
    if key > 26:
        return keySimplifier(key - 26)
    else:
        return key

print(caesarCipherEncryptor("abc", 57))