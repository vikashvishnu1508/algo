def riverSizes(matrix):
    # Write your code here.
    result = []
    haveVisited = [[False for column in range(len(matrix[0]))] for rows in range(len(matrix))]
    for column in range(len(matrix)):
        for row in range(len(matrix[column])):
            if matrix[column][row] == 1 and haveVisited[column][row] == False:
                tempArr = riverSizesHelper(matrix, haveVisited, column, row)
                result.append(tempArr[0])
                haveVisited = tempArr[1]
            else:
                haveVisited[column][row] = True
    return sorted(result)



def riverSizesHelper(matrix, haveVisited, column, row):
    haveVisited[column][row] = True
    counter = 1
    tempArr = []
    if column - 1 >= 0 and matrix[column - 1][row] == 1 and haveVisited[column - 1][row] == False:
        tempArr = riverSizesHelper(matrix, haveVisited, column -1, row)
        counter += tempArr[0]
        haveVisited = tempArr[1]
    if row - 1 >=  0 and matrix[column][row - 1] == 1 and haveVisited[column][row - 1] == False:
        tempArr = riverSizesHelper(matrix, haveVisited, column, row - 1)
        counter += tempArr[0]
        haveVisited = tempArr[1]
    if row + 1 < len(matrix[column]) and matrix[column][row + 1] == 1 and haveVisited[column][row + 1] == False:
        tempArr = riverSizesHelper(matrix, haveVisited, column, row + 1)
        counter += tempArr[0]
        haveVisited = tempArr[1]
    if column + 1 < len(matrix) and matrix[column + 1][row] == 1 and haveVisited[column + 1][row] == False:
        tempArr = riverSizesHelper(matrix, haveVisited, column + 1, row)
        counter += tempArr[0]
        haveVisited = tempArr[1]
    return [counter, haveVisited]


print(riverSizes([
            [1, 1, 0],
            [1, 0, 1],
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 0],
            [1, 0, 0],
            [0, 0, 0],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 1],
        ]))