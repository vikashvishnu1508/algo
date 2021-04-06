def removeIslands(matrix):
    # Write your code here.
    row = len(matrix)
    column = len(matrix[0])
    # visited = [[False for i in range(column)] for j in range(row)]
    for i in range(row):
    	for j in range(column):
    		if matrix[i][j] == 1 and (i == 0 or j == 0 or i == row - 1 or j == column - 1):
    			convertable(matrix, i, j, row, column)
    print(matrix)
    # for i in range(1, row - 1):
    # 	for j in range(1, column - 1):
    # 		if matrix[i][j] == 1 and not visited[i][j]:
    # 			matrix[i][j] = 0

    return matrix


# all values come from the border
def convertable(matrix, i, j, row, column):
    if matrix[i][j] == 2:
        return
    
    matrix[i][j] = 2
	
	# right
    if j + 1 < column and matrix[i][j + 1] == 1:
    	convertable(matrix, i, j + 1, row, column)
	
	# top
    if i + 1 < row and matrix[i + 1][j] == 1:
    	convertable(matrix, i + 1, j, row, column)

	# left
    if j - 1 > 0  and matrix[i][j - 1] == 1:
    	convertable(matrix, i, j - 1, row, column)
	
	# bottom
    if i - 1 > 0  and matrix[i - 1][j] == 1:
    	convertable(matrix, i - 1, j, row, column)

    return

matrix = [
  [1, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 1, 1, 0, 0],
  [1, 0, 0, 0, 0, 1]
]

print(removeIslands(matrix))