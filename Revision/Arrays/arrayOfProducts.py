def arrayOfProducts(array):
    if len(array) == 2:
        array[0], array[1] = array[1], array[0]
        return array
    
    result = []
    firstPdt = 1
    i = 1
    while i < len(array):
        firstPdt *= array[i]
        i += 1
    result.append(firstPdt)

    prevRangePdt = array[0]
    nextRangePdt = firstPdt
    i = 1
    while i < len(array):
        curVal = array[i]
        if curVal != 0:
            nextRangePdt /= curVal
        else:
            nextRangePdt = 0
        result.append(prevRangePdt * nextRangePdt)
        prevRangePdt *= curVal
        i += 1
    return result
# [24, 40, 30, 60]
array = [0, 0, 0, 0]
print(arrayOfProducts(array))