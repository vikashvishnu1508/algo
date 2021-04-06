def threeLargest(array):
    max = [float('-inf'), float('-inf'), float('-inf')]
    i = 0
    while i < len(array):
        if max[2] < array[i]:
            max[0], max[1] = max[1], max[2]
            max[2] = array[i]
        elif max[1] < array[i]:
            max[0] = max[1]
            max[1] = array[i]
        elif max[0] < array[i]:
            max[0] = array[i]
        i += 1
    return max

print(threeLargest([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))