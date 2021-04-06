def levenshteinDistance(str1, str2):
    # Write your code here.
    expected = " " + str2
    given = " " + str1
    arr = [i for i in range(len(expected))]
    for i in range(1, len(given)):
    	arr[0] += 1
    	dia = arr[0]
    	for j in range(1, len(expected)):
    		curDia = arr[j]
    		if expected[j] == given[i]:
    			arr[j] = dia
    		else:
    			arr[j] = min(arr[j], arr[j - 1], dia) + 1
    		dia = curDia
    return arr[-1]

print(levenshteinDistance("abc", "abx"))