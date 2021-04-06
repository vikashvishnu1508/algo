def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    result = [None, None]
    min = abs(arrayOne[0] - arrayTwo[0])
    l1 = 0
    l2 = 0
    while l1 < len(arrayOne) and l2 < len(arrayTwo):
        absDiff = abs(arrayOne[l1] - arrayTwo[l2])
        if absDiff == 0:
            result[0] = arrayOne[l1]
            result[1] = arrayTwo[l2]
            return result
        if min > absDiff:
            min = absDiff
            result[0] = arrayOne[l1]
            result[1] = arrayTwo[l2]
        if arrayOne[l1] < arrayTwo[l2]:
            l1 += 1
        elif arrayOne[l1] > arrayTwo[l2]:
            l2 += 1
    return result

print(smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]))
#[20, 17]