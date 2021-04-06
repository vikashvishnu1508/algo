def riverSizes(matrix):
    # Write your code here.
    rows = len(matrix)
    columns = len(matrix[0])
    river = []

    for i in range(rows):
    	for j in range(columns):
    		if matrix[i][j] == 1:
    			curSize = riverSizesHelper(matrix, i, j, 0)
    			river.append(curSize)
    return river

def riverSizesHelper(matrix, i, j, count):
	if matrix[i][j] == 0:
		return 0
	matrix[i][j] = 0
	
	if i > 0:
		top = riverSizesHelper(matrix, i - 1, j, count)
		count += top
	if i < len(matrix) - 1:
		bottom = riverSizesHelper(matrix, i + 1, j, count)
		count += bottom
	if j > 0:
		left = riverSizesHelper(matrix, i, j - 1, count)
		count += left
	if j < len(matrix[0]) - 1:
		right = riverSizesHelper(matrix, i, j + 1, count)
		count += right
	
	return count +  1

matrix = [
    [1, 1, 0, 0, 0, 0, 1, 1], 
    [1, 0, 1, 1, 1, 1, 0, 1], 
    [0, 1, 1, 0, 0, 0, 1, 1]
    ]

print(riverSizes(matrix))