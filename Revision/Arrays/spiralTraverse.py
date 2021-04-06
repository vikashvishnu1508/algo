def spiralTraverseWithRecursion(array):
    result = []
    visitRange = {
        'firstRow' : 0,
        'lastRow' : len(array),
        'firstColumn' : -1,
        'lastColumn' : len(array[0])
    }
    goRight(array, 0, 0, result, visitRange)
    return result


def goRight(array, i, j, result, visitRange):
    if j >= visitRange['lastColumn']:
        return
    while j < visitRange['lastColumn']:
        result.append(array[i][j])
        j += 1
    visitRange['lastColumn'] = j - 1
    goDown(array, i + 1, j - 1, result, visitRange)

    
def goDown(array, i, j, result, visitRange):
    if i >= visitRange['lastRow']:
        return
    while i < visitRange['lastRow']:
        result.append(array[i][j])
        i += 1
    visitRange['lastRow'] = i - 1
    goLeft(array, i - 1, j - 1, result, visitRange)

def goLeft(array, i, j, result, visitRange):
    if j <= visitRange['firstColumn']:
        return
    while j > visitRange['firstColumn']:
        result.append(array[i][j])
        j -= 1
    visitRange['firstColumn'] = j + 1
    goUp(array, i - 1, j + 1, result, visitRange)
    
def goUp(array, i, j, result, visitRange):
    if i <= visitRange['firstRow']:
        return
    while i > visitRange['firstRow']:
        result.append(array[i][j])
        i -= 1
    visitRange['firstRow'] = i + 1
    goRight(array, i + 1, j + 1, result, visitRange)




















def spiralTraverse(array):
    result = []
    sr, sc = 0, 0
    er = len(array)
    ec = len(array[0])
    while sr < er and sc < ec:
        for col in range(sc, ec):
            result.append(array[sr][col])
        
        for row in range(sr + 1, er):
            result.append(array[row][ec - 1])

        for col in reversed(range(ec, sc)):
            
            result.append(array[er][col])
        
        for row in reversed(range(sr + 1, er)):
            result.append(array[row][sc])

        sr += 1
        ec -= 1
        sc += 1
        er -= 1
    return result








# [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 15, 14, 3, ...]
array = [
    [1, 2, 3, 4], 
    [12, 13, 14, 5], 
    [11, 16, 15, 6], 
    [10, 9, 8, 7]
]

print(spiralTraverse(array))
