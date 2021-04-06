def threeNumberSum1(array, targetSum):
    result = []
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(len(array)):
                if i != j and i != k and j != k:
                    curArr = [array[i], array[j], array[k]]
                    curArr.sort()
                    curSum = sum(curArr)
                    if curSum == targetSum and curArr not in result:
                        result.append(curArr)
    return result


def threeNumberSum(array, targetSum):
    array.sort()
    # [-8, -6, 1, 2, 3, 5, 6, 12]
    result = []
    print(array)
    for first in range(len(array) - 2):
        second = first + 1
        third = len(array) - 1
        currentTarget = targetSum - array[first]
        while second < third:
            currentSum = array[second] + array[third]
            if currentSum == currentTarget:
                result.append([array[first], array[second], array[third]])
                second += 1
                third -= 1
            elif currentSum < currentTarget:
                second += 1
            elif currentSum > currentTarget:
                third -= 1
    return result







array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))