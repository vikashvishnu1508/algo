def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left < right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binarySearch([1, 5, 23, 111], 111))