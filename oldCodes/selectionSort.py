def selectionSort(array):
    # Write your code here.
    i = 0
    while i < len(array) - 1:
    	min_index = i
    	j = i + 1
    	while j < len(array):
    		if array[j] < array[min_index]:
    			min_index = j
    		j += 1
    	array[i], array[min_index] = array[min_index], array[i]
        i += 1
    return array

print(selectionSort([8, 5, 2, 9, 5, 6, 3]))