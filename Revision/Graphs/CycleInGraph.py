
def cycleInGraph(edges):
    # Write your code here.
	for curVertex in range(len(edges)):
		if isACycle(curVertex, edges, curVertex, {}):
			return True
	return False
			
def isACycle(target, edges, curVertex, visited):
	if curVertex in visited:
		return True
	visited[curVertex] = True
	
	for edge in edges[curVertex]:
		if target == edge:
			return True	
		if isACycle(target, edges, edge, visited):
			return True
		
	visited[curVertex] = False
	
	return False



print(cycleInGraph([
  [1, 2],
  [2],
  [1]])
)