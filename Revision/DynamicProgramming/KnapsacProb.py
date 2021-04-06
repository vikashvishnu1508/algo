def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    if len(items) == 0:
    	return [0, []]

    maxCap = [[0 for col in range(capacity + 1)] for row in range(len(items))]

    for row in range(len(maxCap)):
    	value = items[row][0]
    	weight = items[row][1]
    	for col in range(1, len(maxCap[row])):
    		curCapacity = col
    		if curCapacity == weight:
    			maxCap[row][col] = value
    		if row == 0:
    			maxCap[row][col] = max(maxCap[row][col], maxCap[row][col - 1])
    			continue
            
    		prevWeight = curCapacity - weight
    		if prevWeight < 1 :
    			maxCap[row][col] = max(maxCap[row][col], maxCap[row][col - 1], maxCap[row - 1][col])
    			continue
            
    		valAtPrevWeight = maxCap[row - 1][prevWeight]
    		if valAtPrevWeight + value > maxCap[row][col]:
    			maxCap[row][col] = valAtPrevWeight + value
    
    		maxCap[row][col] = max(maxCap[row][col], maxCap[row][col - 1], maxCap[row - 1][col])

    print(maxCap)
    totValue = maxCap[-1][-1]
    index = []
    i = len(maxCap) - 1
    j = len(maxCap[i]) - 1

    while i >= 0 and j >= 0:
        if maxCap[i][j] == maxCap[i - 1][j]:
        	i -= 1
        else:
            index.append(i)
            weight = items[i][1]
            j -= weight

        if i == 0:
	        if maxCap[i][j] == maxCap[i + 1][j]:
	    	    index.append(i)
        

    return [totValue, list(reversed(index))]			

items = [[1, 2], [4, 3], [5, 6], [6, 9]]
capacity = 11

print(knapsackProblem(items, capacity))

