def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            newSum = array[i] + array[left] + array[right]
            if newSum == targetSum:
                result.append([array[i], array[left], array[right]])
                if len(result) == 3:
                    return result
                left += 1
                right -= 1
            elif newSum < targetSum:
                left += 1
            elif newSum > targetSum:
                right -= 1
    return result



print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))