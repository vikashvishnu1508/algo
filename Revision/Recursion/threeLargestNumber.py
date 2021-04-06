array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

def findThreeLargestNumbers(array):
    result = [None for i in range(3)]
    for num in array:
        updateResults(result, num)
    return result

def updateResults(result, num):
    for i in reversed(range(3)):
        if result[i] is None:
            result[i] = num
            return
        elif result[i] < num:
            j = i
            curVal = num
            while j >= 0:
                replaceValue = result[j]
                result[j] = curVal
                curVal = replaceValue
                j -= 1
            return


print(findThreeLargestNumbers(array))