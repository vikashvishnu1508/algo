def kadanesAlgorithm(array):
    # Write your code here.
    i = 1
    result = array[0]
    maxSum = array[0]
    while i < len(array):
        maxSum = max(maxSum + array[i], array[i])
        result = max(maxSum, result)
        i += 1
    return result

print(kadanesAlgorithm([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
