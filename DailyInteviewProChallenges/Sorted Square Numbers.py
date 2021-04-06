def square_numbers(nums):
    square_numbersArr = []
    lastNegativeSquareIdx = -1
    i = 0
    while i < len(nums):
        if nums[i] < 0:
            lastNegativeSquareIdx = i
        elif nums[i] >= 0:
            curValueSquare = nums[i]**2
            if lastNegativeSquareIdx >= 0:
                lastNegativeSquare = nums[lastNegativeSquareIdx]**2
                if lastNegativeSquare <= curValueSquare:
                    square_numbersArr.append(lastNegativeSquare)
                    lastNegativeSquareIdx -= 1
                    continue
                else:
                    square_numbersArr.append(curValueSquare)
            else:
                square_numbersArr.append(curValueSquare)
        i += 1
    
    while lastNegativeSquareIdx >= 0:
        square_numbersArr.append(nums[lastNegativeSquareIdx]**2)
        lastNegativeSquareIdx -= 1

    return square_numbersArr







print(square_numbers([-8, -5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]