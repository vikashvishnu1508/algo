def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    if width == height == 0:
    	return 0
    if width == 1:
    	return 1

    layout = [[1 if col == 0 else 0 for col in range(width)] for row in range(height)]

    for row in range(height):
    	for col in range(width):
    		if row == 0 :
    			layout[row][col] = 1
    		else:
    			layout[row][col] = layout[row - 1][col] + layout[row][col - 1]

    return layout




result = numberOfWaysToTraverseGraph(10, 10)

for i in result:
    print(i)
        


# for width in range(1, 10):
#     print(f"-------------------{width}-------------------------------------")
#     for height in range(1, 10):
#         result = numberOfWaysToTraverseGraph(width, height)
#         print(f"width = {width}, height = {height}, result = {result}")
#     print(f"--------------------------------------------------------")
