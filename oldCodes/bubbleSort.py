def bubbleSort(array):
    # Write your code here.
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        counter += 1
    return array

print(bubbleSort([76,4,67,8,2]))

# [-10, -7, -7, -6, -6, -5, -5, -4, -4, -4, -2, -1, 1, 3, 5, 5, 6, 8, 8, 10]