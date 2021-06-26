def reverseWord(string):
    reversedString = []
    stack = []
    for char in string:
        if char == ' ':
            while len(stack):
                reversedString.append(stack.pop())
            reversedString.append(char)
        else:
            stack.append(char)
    while len(stack):
        reversedString.append(stack.pop())
    return ''.join(reversedString)

print(reverseWord("test this string"))