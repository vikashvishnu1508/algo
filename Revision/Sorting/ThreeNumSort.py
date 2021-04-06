def threeNumSort(array, order):
    first = 0
    second = 0
    third = len(array) - 1
    while second <= third:
        if array[second] == order[0]:
            array[first], array[second] = array[second], array[first]
            first += 1
            second += 1
        elif array[second] == order[2]:
            array[second], array[third] = array[third], array[second]
            third -= 1
        else:
            second += 1
    return array




print(threeNumSort([1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1]))