def smallestDifference1(arrayOne, arrayTwo):
    # Write your code here.
    minimum = float('inf')
    result = [None, None]
    for i in arrayOne:
    	for j in arrayTwo:
    		if abs(i - j) < minimum:
    			minimum = abs(i - j)
    			result[0], result[1] = i, j
    return result


def smallestDifference(arrayOne, arrayTwo):
    result = [None, None]
    minimum = float('inf')
    arrayOne.sort()
    arrayTwo.sort()
    # arrayOne = [-1, 3, 5, 10, 20, 28]
    # arrayTwo = [15, 17, 26, 134, 135]
    # if len(arrayOne) >= len(arrayTwo):
    #     longest = len(arrayOne)
    #     shortest = len(arrayTwo)
    # else:
    #     longest = len(arrayTwo)
    #     shortest = len(arrayOne)
    i = 0
    j = 0
    while i < len(arrayOne) and j < len(arrayTwo):
        curAbsDiff =  abs(arrayOne[i] - arrayTwo[j])
        if curAbsDiff < minimum:
            minimum = curAbsDiff
            result[0], result[1] = arrayOne[i], arrayTwo[j]
        # execute this any case
        if arrayOne[i] < arrayTwo[j]:
            i += 1
        else:
            j += 1
    if i == len(arrayOne) and j < len(arrayTwo):
        i = i - 1
        while j < len(arrayTwo):
            curAbsDiff = abs(arrayOne[i] - arrayTwo[j])
            if curAbsDiff < minimum:
                minimum = curAbsDiff
                result[0], result[1] = arrayOne[i], arrayTwo[j]
            j += 1
        
    elif i < len(arrayOne) and j == len(arrayTwo):
        j = j - 1
        while i < len(arrayOne):
            curAbsDiff = abs(arrayOne[i] - arrayTwo[j])
            if curAbsDiff < minimum:
                minimum = curAbsDiff
                result[0], result[1] = arrayOne[i], arrayTwo[j]
            i += 1

    return result
        





arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo))