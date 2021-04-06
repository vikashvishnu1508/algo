array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
result= [0, 0, 0, 1, 1, 1, -1, -1]

def threeNumSort(array, order):
    first = 0
    second = 0
    third = len(array) - 1

    for i in range(len(array)):
        if array[i] == order[0]:
            second += 1
        elif array[i] == order[2]:
            third -= 1
    
    for i in range(len(array)):
        if i < second:
            array[i] = order[0]
        elif i >= second and i <= third:
            array[i] = order[1]
        else:
            array[i] = order[2]
    return array

print(threeNumSort(array, order))