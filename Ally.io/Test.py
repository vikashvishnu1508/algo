input1 = 'azbxrtycoip'

def getLongestPanlindrome(string):
    maxLength = 0
    for i in range(len(string)):
        evenPalindromDistance = checkPalindrome(string, i, True)
        oddPalindromDistance = checkPalindrome(string, i, False)
        maxLength = max(maxLength, evenPalindromDistance, oddPalindromDistance)
    return maxLength

def checkPalindrome(string, idx, isEven):
    distance = 0
    left = idx if isEven else idx - 1 
    right = idx + 1
    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            distance += 1
            left -= 1
            right += 1
        else:
            break
    if distance == 0:
        return 0

    if isEven:
        return distance * 2
    else:
        return (distance * 2) + 1


print(getLongestPanlindrome(input1))
