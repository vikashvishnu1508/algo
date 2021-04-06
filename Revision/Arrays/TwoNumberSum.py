def twoNumberSumMethod1(array, target):
    lastSeen = {}
    for i in array:
        expectedValue = target - i
        if expectedValue not in lastSeen:
            lastSeen[i] = True
        else:
            return [i, expectedValue]
    return [-1, -1]

def twoNumberSumMethod2(array, target):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        expectedValue = target - array[left]
        if array[right] == expectedValue:
            return [array[left], array[right]]
        elif array[right] > expectedValue:
            right -= 1
        left += 1
    return [-1, -1]





array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

print(twoNumberSumMethod1(array, targetSum))
print(twoNumberSumMethod2(array, targetSum))