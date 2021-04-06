def hourglassSum(arr):
    sum = 0
    max = 0
    for k in range(16):
        for i in range(len(arr)):
            if i < 0+(k//4):
                pass
            if i > 2+(k//4):
                break
            for j in range(len(arr[i])):
                if j <  0 + (k%4):
                    pass
                if j > 2 + (k%4):
                    break
                if (i == 0+(k//4) or i == 2+(k//4)) and j >= 0 + (k%4) and j <= 2 + (k%4):
                    sum += arr[i][j]
                if i == 1 + (k//4) and j == 1  + (k%4):
                    sum += arr[i][j]
        # print('sum = ',sum)
        # print('max = ',max)
        if k == 0 or max < sum:
            max = sum
        sum = 0
    return max

my_arr = '''0 -4 -6 0 -7 -6
-1 -2 -6 -8 -3 -1
-8 -4 -2 -8 -8 -6
-3 -1 -2 -5 -7 -4
-3 -5 -3 -6 -6 -6
-3 -6 0 -8 -6 -7'''

arr = []
for i in my_arr.splitlines():
        arr.append(list(map(int, i.rstrip().split())))

print(hourglassSum(arr))