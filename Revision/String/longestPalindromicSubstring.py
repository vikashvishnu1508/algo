def longestPalindromicSubstring(string):
    longestPalindrome = [-1, -1]
    longestLength = 0

    for i in range(1, len(string) - 1):
        curPalindrome = []

        if string[i - 1] == string[i]:
            curPalindrome = expandOutwards(string, i - 1, i)
        elif string[i - 1] == string[i + 1]:
            curPalindrome = expandOutwards(string, i - 1, i + 1)
        
        if len(curPalindrome) != 0:
            curLength = (curPalindrome[1] - curPalindrome[0]) + 1
            if curLength > longestLength:
                longestLength = curLength
                longestPalindrome = curPalindrome
    
    return string[longestPalindrome[0] : longestPalindrome[1] + 1]

def expandOutwards(string, left, right):
    while left >= 0 and right < len(string):
        if string[left] == string[right]:
            left -= 1
            right += 1
        else:
            break
    left += 1
    right -= 1
    return [left, right]


string = "abaxyzzyxf"
print(longestPalindromicSubstring(string))