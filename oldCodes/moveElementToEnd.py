def moveElementToEnd(array, toMove):
    # Write your code here.
    i = 0
    placer = 0
    while i < len(array):
        if array[i] != toMove:
            swap(array, i, placer)
            placer += 1
        i += 1
    return array


def swap(array, i, placer):
    array[i], array[placer] = array[placer], array[i]


print(moveElementToEnd([1,2,3,4,5], 28))