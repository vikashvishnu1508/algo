array = [5, 3, 4, -1, 1]
array1 = [1, 2, 0]
array2 = [-4,-5,-7,-1,0]

def firstMissingNumber(array):
    smallerNum = None
    biggerNum = None
    for number in array:
        if smallerNum is None or smallerNum == number:
            smallerNum = assignSmallerVal(number)
        elif biggerNum is None or biggerNum == number:
            biggerNum = assignBiggerVal(number)
    
    if biggerNum is None and smallerNum is None:
        return 1
    elif smallerNum is None:
        return biggerNum
    elif biggerNum is None:
        return smallerNum
    else:
        return min(smallerNum, biggerNum)
        
        
        # if number in (smallerNum, biggerNum):
        #     if smallerNum == number:
        #         smallerNum = None
        #     if biggerNum == number:
        #         biggerNum = None
        #     continue

def assignSmallerVal(number):
    return number - 1 if number - 1 >= 1 else None

def assignBiggerVal(number):
    return number + 1 if number + 1 >= 1 else None

#####################################################################################
def firstMissingNumberUsingDictonary(array):
    numDictnary = {i : True for i in array}
    leastMissingNumber = float('inf')
    maxElement = -float('inf')
    for num in array:
        maxElement = max(maxElement, num)
        if num <= 0 or num - 1 <= 0:
            continue
        elif num - 1 in numDictnary:
            continue
        else:
            curLesserVal = iterativeForPrevNumber(numDictnary, num)
            leastMissingNumber = min(leastMissingNumber, curLesserVal)
    if leastMissingNumber == float('inf'):
        return maxElement + 1 if maxElement > 0 else 1
    else:
        return leastMissingNumber

def iterativeForPrevNumber(numDictnary, number):
    i = number - 1
    # flag = False
    while i > 0 and i not in numDictnary:
        # flag = True
        i -= 1
    # return i + 1 if flag else i
    return i + 1

#####################################################################################

# O(N log N) - sorting
def firstMissingNumberUsingSorting(array):
    array.sort()
    if array[0] >= 2:
        return 1
    prevLesserVal = None
    for num in array:
        if num <= 0:
            continue
        else:
            if prevLesserVal is None and num >= 2:
                return 1
            elif prevLesserVal is None and num < 2:
                prevLesserVal = num
            else:
                if num - 1 > prevLesserVal:
                    return prevLesserVal + 1
                elif num - 1 == prevLesserVal:
                    prevLesserVal = num
                else:
                    prevLesserVal = num
                    print(f"peculier case: num = {num}, prevLesserVal = {prevLesserVal}")
    if prevLesserVal is None:
        return 1
    else:
        return prevLesserVal + 1

#####################################################################################

print(firstMissingNumber(array))



