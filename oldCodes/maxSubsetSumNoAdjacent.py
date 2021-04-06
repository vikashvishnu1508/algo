def maxSubsetSumNoAdjacent(array):
    second = array[0]
    first = max(array[0], array[1])
    current = 0
    i = 2
    while i < len(array):
        current = max(first, array[i] + second)
        second = first
        first = current
        i = i + 1
    return max(first, second)

print(maxSubsetSumNoAdjacent([7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4]))