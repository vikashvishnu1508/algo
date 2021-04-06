def closest_3sum(nums, target):    
    closest_3sumArr = [float('inf'), float('inf'), float('inf')]
    maxNumDiff = float('inf')
    for num in nums:
        curNumDiff = abs(target - num)
        if curNumDiff < maxNumDiff:
            if num > closest_3sumArr[-1]:
                closest_3sumArr = replaceOrderBigNum(closest_3sumArr, num)
            else:
                closest_3sumArr = replaceOrderSmallNum(closest_3sumArr, num)
            maxNumDiff = abs(target - closest_3sumArr[-1])
        
    return closest_3sumArr

def replaceOrderSmallNum(array, number):
    i = 0
    startReplace = False
    while i < len(array):
        if startReplace:
            curNum = array[i]
            array[i] = replaceNum
            replaceNum = curNum
        if not startReplace and array[i] > number:
            startReplace = True
            replaceNum = array[i]
            array[i] = number
        i += 1
    return array

def replaceOrderBigNum(array, number):
    i = 2
    startReplace = False
    while i >= 0:
        if array[i] is None:
            array[i] = number
            return array
        if startReplace:
            curNum = array[i]
            array[i] = replaceNum
            replaceNum = curNum
        if not startReplace and array[i] < number:
            startReplace = True
            replaceNum = array[i]
            array[i] = number
        i -= 1
    return array


print(closest_3sum([7, 8, 9, 20, 2, 1, -5, 4], 3))
# Closest sum is -5+1+2 = -2 OR -5+1+4 = 0
# print [-5, 1, 2]