import math

def is_palindrome(n):
    numOfDigits = getNumberOfDigits(n)
    while n > 9:
        lastNum = n % 10
        n = n // 10
        numOfDigits -= 1
        curDivisor = getDivisorValByDigits(numOfDigits)
        firstNum = n // curDivisor if n // curDivisor > 0 else n
        numOfDigits -= 1
        n = n % curDivisor
        if firstNum != lastNum:
            return False
    
    return True


def getDivisorValByDigits(numOfDigits):
    divisor = 10
    for _ in range(numOfDigits - 2):
        divisor *= 10
    return divisor

def getNumberOfDigits(num):
    numOfDigits = 0
    while num > 0:
        num = num // 10
        numOfDigits += 1
    return numOfDigits

print(is_palindrome(1234564321))
# True
# print(is_palindrome(1234322))
# # False