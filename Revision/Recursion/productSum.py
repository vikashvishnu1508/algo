# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    # Write your code here.
    return getSum(array, 1)


def getSum(array, depth):
	print(f"array = {array}")
	productSum = 0
	for curItem in array:
		print(f"curItem = {curItem}, productSum = {productSum}")
		if isinstance(curItem, list):
			productSum += getSum(curItem, depth + 1)
			print(f"is a list productSum = {productSum}")
		else:
			productSum += (depth * curItem)
			print(f"else productSum = {productSum}")
	return productSum

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]

print(productSum(array))