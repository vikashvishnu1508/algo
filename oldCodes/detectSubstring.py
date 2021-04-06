def detectSubstring(s, subStr):
    for i in range(len(s) - len(subStr)):
        if s[i:i+len(subStr)] == subStr:
            return i
    return -1


print( detectSubstring('thepigflewwow', 'flew'))