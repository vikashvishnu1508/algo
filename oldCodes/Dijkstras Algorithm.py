def dijkstrasAlgorithm(start, edges):
	# Write your code here.
	visitedNodes = {}
	nodeByVal = [float('inf') if i != start else 0 for i in range(len(edges))]
	updateNodeValues(start, edges, visitedNodes, nodeByVal)
	for i in range(len(nodeByVal)):
		if nodeByVal[i] == float('inf'):
			nodeByVal[i] = -1
	return nodeByVal
    

def updateNodeValues(start, edges, visitedNodes, nodeByVal):
	currentMinIdx = start
	while currentMinIdx != float('inf'):
		curNode = edges[currentMinIdx]
		# d(u)
		curNodeValue = nodeByVal[currentMinIdx]
		for node, weight in curNode:
			# c(u, v)
			targetNodeDistance = weight
			# d(v)
			targetNodeValue = nodeByVal[node]
			if targetNodeValue > curNodeValue + targetNodeDistance:
				nodeByVal[node] = curNodeValue + targetNodeDistance
		visitedNodes[currentMinIdx] = True
		minVal = float('inf')
		minIdx = float('inf')
		for i in range(len(nodeByVal)):
			if i in visitedNodes:
				continue
			if minVal > nodeByVal[i]:
				minVal = nodeByVal[i]
				minIdx = i
		currentMinIdx = minIdx

edges = [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]
start = 0

print(dijkstrasAlgorithm(start, edges))
