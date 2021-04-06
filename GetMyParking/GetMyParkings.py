input1 = [1, 2]
output = [10,10,9,9,9,9,9,1,0]



# Time - O(N)
# Space - O(N)

def getTheGretestInRightSide(array):
    if len(array) <= 1:
        return [0]
    
    result = []
    for _ in array:
        result.append(0)
    
    curMax = 0
    i = len(array) - 2

    while  i >= 0:
        curMax = max(curMax, array[i + 1])
        result[i] = curMax
        i -= 1
    
    return result



print(getTheGretestInRightSide(input1))

