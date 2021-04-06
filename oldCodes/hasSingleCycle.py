def hasSingleCycle(array):
    counter = [0 for i in array]
    i = 0
    while True:
        counter[i] += 1
        if counter[i] > 1:
            break
        currentIndex = i + array[i]
        i = currentIndex % len(array)
    i = 0
    for i in range(len(counter)):
        if i == 0 and counter[i] != 2:
            return False
        if i > 0 and counter[i] != 1:
            return False
    return True

print(hasSingleCycle([1, 1, 1, 1, 2]))