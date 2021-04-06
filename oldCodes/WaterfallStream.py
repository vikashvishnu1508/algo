down = 'down'
left = 'left'
right = 'right'

def waterfallStreams(array, source):
	# Write your code here.
	capturedWater = [0 for i in range(len(array[0]))]
	checkForBlockage(array, 1, 0, source, capturedWater, down)
	return capturedWater
	
def checkForBlockage(array, unit, i, j, capturedWater, direction):
	if i == len(array) - 1:
		print(f"reached last row i = {i}, j = {j}")
		capturedWater[j] += (unit * 100)
		return
	if array[i + 1][j] == 0:
		return checkForBlockage(array, unit, i + 1, j, capturedWater, down)
	else:
		# left and right both blocked
		if j - 1 >= 0 and j + 1 < len(array[0]) and array[i][j + 1] == array[j - 1] == 1:
			return
		elif direction == down:
			# left and right both open
			if j - 1 >= 0 and j + 1 < len(array[0]) and array[i][j + 1] == array[i][j - 1] == 0:
				checkForBlockage(array, unit / 2, i, j - 1, capturedWater, left)
				checkForBlockage(array, unit / 2, i, j + 1, capturedWater, right)
				return
			# left is start and right is blockeed
			elif j == 0 and j + 1 < len(array[0]) and array[i][j + 1] == 1:
				return
			# left block and right open - go to right
			elif j - 1 >= 0 and j + 1 < len(array[0]) and array[i][j - 1] == 1 and array[i][j + 1] == 0:
				return checkForBlockage(array, unit / 2, i, j + 1, capturedWater, right)
			# left is start and right is opon - go to right
			elif j == 0 and j + 1 < len(array[0]) and array[i][j + 1] == 0:
				return checkForBlockage(array, unit / 2, i, j + 1, capturedWater, right)

			# right is end and left is blocked
			elif j == len(array[0]) - 1 and j - 1 >= 0  and array[i][j - 1] == 1:
				return
			# right is block and left is open - go to left
			elif j - 1 >= 0 and j + 1 < len(array[0]) and array[i][j - 1] == 0 and array[i][j + 1] == 1:
				return checkForBlockage(array, unit / 2, i, j - 1, capturedWater, left)
			# right is end and left is open - go to left
			elif j == len(array[0]) - 1 and j - 1 >= 0  and array[i][j - 1] == 0:
				return checkForBlockage(array, unit / 2, i, j - 1, capturedWater, left)
		
		elif direction == left:
			if j == 0:
				return
			elif j - 1 >= 0 and array[i][j - 1] == 1:
				return
			elif j - 1 >= 0 and array[i][j - 1] == 0:
				return checkForBlockage(array, unit, i, j - 1, capturedWater, left)
		elif direction == right:
			if j == len(array[0]) - 1:
				return
			elif j + 1 < len(array[0]) and array[i][j + 1] == 1:
				return
			elif j + 1 < len(array[0]) and array[i][j + 1] == 0:
				return checkForBlockage(array, unit, i, j + 1, capturedWater, right)

	
	

array = [
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0]
]
source = 3

print(waterfallStreams(array, source))