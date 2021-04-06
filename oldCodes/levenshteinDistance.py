def levenshteinDistance(str1, str2):
    # Write your code here.
    e = [[None for column in range(len(str2) + 1)]for row in range(len(str1) + 1)]
    for row in range(len(str1) + 1):
        for col in range(len(str2) + 1):
            # print('row = ', row)
            # print('col = ', col)
            # print('e[row][col] = ', e[row][col])
            if row == 0 and col == 0:
                e[row][col] = 0
            elif row == 0 and col != 0:
                e[row][col] = col
            elif row != 0 and col == 0:
                e[row][col] = row
            else:
                if str1[row - 1] == str2[col - 1]:
                    e[row][col] = e[row - 1][col - 1]
                else:
                    e[row][col] = 1 + min(e[row - 1][col], e[row][col -1], e[row -1][col - 1])
    print(e)

print(levenshteinDistance('uvw', 'stuv'))