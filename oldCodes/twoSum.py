def twoNumberSum(array, targetSum):
    # Write your code here.
    dicu ={}
    for i in array:
        dicu[i] = i
    for i in array:
        try:
            secondOne = targetSum - i
            if targetSum - i == dicu.get(secondOne) and dicu.get(secondOne) != i:
                return [i, secondOne]
        except:
            pass
    return []
	# for i in range(len(array) - 1):
	# 	for j in range(i + 1, len(array)):
	# 		if array[i] + array[j] == targetSum:
	# 			return [array[i], array[j]]

print(twoNumberSum([4,6,1],5))