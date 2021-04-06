string = "xyz"
key = 2

def caesarCipherEncryptor(string, key):
    keyVal = key % 26
    charArr = [chr(getNewLetter(letter, keyVal)) for letter in string]
    return ''.join(charArr)

def getNewLetter(letter, key):
    newVal = ord(letter) + key
    return newVal if newVal <= 122 else (96 + newVal) % 122
    



print(caesarCipherEncryptor(string, key))