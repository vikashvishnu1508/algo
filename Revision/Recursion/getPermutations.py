def getPermutations(array):
    # Write your code here.
    perms = []
    generate(array, [], perms)
    return perms


def generate(array, cur, perms):
	if len(array) == 0 and len(cur) > 0:
		perms.append(cur)
	else:
		for i in range(len(array)):
			newArr = array[ : i] + array[i + 1 : ]
			newPerm = cur + [array[i]]
			generate(newArr, newPerm, perms)
	

array = [1, 2, 3]
print(getPermutations(array))
