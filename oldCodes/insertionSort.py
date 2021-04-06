def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        temp = array[i]
        j = i
        while temp < array[j - 1] and j > 0:
            #until
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp
    return array

        # key = arr[i] 
        # j = i-1
        # while j >= 0 and key < arr[j] : 
        #         arr[j + 1] = arr[j] 
        #         j -= 1
        # arr[j + 1] = key

print(insertionSort([8, 5, 2, 9, 5, 6, 3]))
