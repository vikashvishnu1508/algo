def waterArea(heights):
    # Write your code here.
    area = 0
    water = [0 for i in heights]
    leftMax = 0
    for i in range(len(heights)):
    	water[i] = leftMax
    	leftMax = max(heights[i], leftMax)

    rightMax = 0
    for i in reversed(range(len(heights))):
    	flag = False
    	if water[i] == 0 or rightMax == 0:
    		flag = True
    	minVal = min(rightMax, water[i])
    	if minVal < heights[i]:
    		flag = True
    
    	if not flag:
    		area += (minVal - heights[i])
    
    	water[i] = rightMax
    	rightMax = max(heights[i], rightMax)
    
    	return area
	
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(waterArea(heights))

h = [0,  8,  0,  0,  5,  0,  0, 10, 0,  0,  1,  1,  0,  3]
l = [0,  0,  8,  8,  8,  8,  8,  8, 10, 10, 10, 10, 10, 10]
r = [10, 10, 10, 10, 10, 10, 10, 3, 3,  3,  3,  3,  3,  0]

