# O(n logn) Time and O(1) Space
def isMonotonic(array):
    if len(array) <= 1:
        return True
    lastOrder = ''
    i = 1
    while i < len(array):
        
        if array[i - 1] < array[i]:
            if lastOrder != '' and lastOrder == 'decreasing':
                return False
            lastOrder = 'increasing'
        elif array[i - 1] > array[i]:
            if lastOrder != '' and lastOrder == 'increasing':
                return False
            lastOrder = 'decreasing'
        i += 1
    return True



array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]

print(isMonotonic(array))
