def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
    	return array
    dupArr = array[:]
    mergeHelper(array, dupArr, 0, len(array) - 1)
    return array


def mergeHelper(mainArr, dupArr, startIdx, endIdx):
	if startIdx == endIdx:
		return
	midIdx = (startIdx + endIdx) // 2
	mergeHelper(mainArr, dupArr, startIdx, midIdx)
	mergeHelper(mainArr, dupArr, midIdx + 1, endIdx)
	merge(mainArr, dupArr, startIdx, midIdx, endIdx)
	
def merge(mainArr, dupArr, startIdx, midIdx, endIdx):
	print(f"startIdx = {startIdx}")
	print(f"midIdx = {midIdx}")
	print(f"endIdx = {endIdx}")
	print("before = ",mainArr)
	k = startIdx
	i = startIdx
	j = midIdx + 1
	
	while i <= midIdx and j <= endIdx:
		if dupArr[i] < dupArr[j]:
			mainArr[k] = dupArr[i]
			i += 1
		else:
			mainArr[k] = dupArr[j]
			j += 1
		k += 1
	
	while i <= midIdx:
		mainArr[k] = dupArr[i]
		i += 1
		k += 1
		
	while j <= endIdx:
		mainArr[k] = dupArr[j]
		j += 1
		k += 1
	print("after = ",mainArr)

print(mergeSort([8, 5, 2, 9, 5, 6, 3]))