def searchInSortedMatrix(matrix, target):
    # Write your code here.
    top = 0
    bottom = len(matrix) - 1
    while top <= bottom:
        horozontalMiddle = (top + bottom) // 2
        if matrix[horozontalMiddle][len(matrix[horozontalMiddle]) // 2] < target:
            top = horozontalMiddle + 1
        elif matrix[horozontalMiddle][len(matrix[horozontalMiddle]) // 2] > target:
            bottom = horozontalMiddle - 1
        left = 0
        right = len(matrix[horozontalMiddle]) - 1
        while left <= right:
            verticalMiddle = (left + right) // 2
            if matrix[horozontalMiddle][verticalMiddle] == target:
                return [horozontalMiddle, verticalMiddle]
            elif matrix[horozontalMiddle][verticalMiddle] < target:
                left = verticalMiddle + 1
            elif matrix[horozontalMiddle][verticalMiddle] > target:
                right = verticalMiddle - 1
    return [-1, -1]

def searchInSortedMatrixClmn(matrix, target):
    top = 0
    bottom = len(matrix) - 1
    # left = 0
    right = len(matrix[0]) - 1
    while right >= 0:
        if matrix[top][right] == target:
            return [top, right]
        elif matrix[top][right] > target:
            right -= 1
        elif matrix[top][right] < target and matrix[bottom][right] >= target:
            while top <= bottom:
                verticalMiddle = (top + bottom) // 2
                if matrix[verticalMiddle][right] == target:
                    return[verticalMiddle, right]
                elif matrix[verticalMiddle][right] > target:
                    bottom = verticalMiddle - 1
                elif matrix[verticalMiddle][right] < target:
                    top = verticalMiddle + 1
            right -= 1
            top = 0
            bottom = len(matrix) - 1
        else:
            return [-1, -1]
    return [-1, -1]

def searchInSortedMatrixClmnRow(matrix, target):
    top = 0
    bottom = len(matrix) - 1
    # left = 0
    right = len(matrix[0]) - 1
    while right >= 0 and top <= bottom:
        if matrix[top][right] == target:
            return [top, right]
        elif matrix[top][right] > target:
            right -= 1
        elif matrix[top][right] < target:
            top += 1
    return [-1, -1]



matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
print(searchInSortedMatrixClmnRow(matrix, 44))