def spinRings(array):
    # Write your code here.
    sizeOfArray = len(array)
    diagonalShiftRange = sizeOfArray // 2
    print(diagonalShiftRange)
    for i in range(diagonalShiftRange):
    	rightShiftedValue = shiftValueInRightSide(array, sizeOfArray, i)
    	downShiftedValue = shiftValueInDownSide(array, sizeOfArray, i, rightShiftedValue)
    	leftShiftedValue = shiftValueInLeftSide(array, sizeOfArray, i, downShiftedValue)
    	shiftValueInUpSide(array, sizeOfArray, i, leftShiftedValue)

    return array		

def shiftValueInRightSide(array, sizeOfArray, idxFromDiagonal):
	print("start")
	replaceValue = None
	for j in range(idxFromDiagonal, sizeOfArray - idxFromDiagonal):
		print(j)
		curPositionValue = array[idxFromDiagonal][j]
		array[idxFromDiagonal][j] = replaceValue
		replaceValue = curPositionValue
		# array[idxFromDiagonal][j] = array[idxFromDiagonal][j - 1]
	return replaceValue

def shiftValueInDownSide(array, sizeOfArray, idxFromDiagonal, replaceValue):
	for i in range(idxFromDiagonal + 1, sizeOfArray - idxFromDiagonal):
		curPositionValue = array[i][(sizeOfArray - 1) - idxFromDiagonal]
		array[i][(sizeOfArray - 1) - idxFromDiagonal] = replaceValue
		replaceValue = curPositionValue
		
	return replaceValue

def shiftValueInLeftSide(array, sizeOfArray, idxFromDiagonal, replaceValue):
	for j in reversed(range(idxFromDiagonal, (sizeOfArray - 1) - idxFromDiagonal)):
		curPositionValue = array[(sizeOfArray - 1) - idxFromDiagonal][j]
		array[(sizeOfArray - 1) - idxFromDiagonal][j] = replaceValue
		replaceValue = curPositionValue
	return replaceValue
		
def shiftValueInUpSide(array, sizeOfArray, idxFromDiagonal, replaceValue):
	for i in reversed(range(idxFromDiagonal, (sizeOfArray - 1) - idxFromDiagonal)):
		curPositionValue = array[i][idxFromDiagonal]
		array[i][idxFromDiagonal] = replaceValue
		replaceValue = curPositionValue
		

print(spinRings([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]))