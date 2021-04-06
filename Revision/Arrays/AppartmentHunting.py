def apartmentHunting(blocks, reqs):
    # Write your code here.
    dist = [float('inf') for i in range(len(blocks))]

    for i in range(len(blocks)):
    	curDist = 0
    	for req in reqs:
    		if blocks[i][req]:
    			continue
    		print(f"i = {i}, req = {req}")
    		prevDist = 0
    		for k in reversed(range(i)):
    			prevDist += 1
    			if blocks[k][req]:
    				break
    			if k == 0:
    				prevDist = 0
    
    		nextDist = 0
    		for k in range(i + 1, len(blocks)):
    			nextDist += 1
    			if blocks[k][req]:
    				break
    			if k == len(blocks) - 1:
    				k = 0
    
    		if prevDist != 0 and nextDist != 0:
    			curMinDistance = min(prevDist, nextDist)
    		else:
    			curMinDistance = max(prevDist, nextDist)
    
    		print(f"prevDist = {prevDist}, nextDist = {nextDist}, curMinDistance = {curMinDistance}")
    
    		curDist = max(curDist, curMinDistance)
    		print(f"curDist = {curDist}")
    
    	dist[i] = curDist

    print(dist)

    minIdx = 0
    for i in range(len(dist)):
    	if dist[i] < dist[minIdx]:
    		minIdx = i

    return minIdx


blocks = [
  {"gym": False, "office": True, "school": True, "store": False},
  {"gym": True, "office": False, "school": False, "store": False},
  {"gym": True, "office": False, "school": True, "store": False},
  {"gym": False, "office": False, "school": True, "store": False},
  {"gym": False, "office": False, "school": True, "store": True}
]
reqs = ["gym", "office", "school", "store"]

print(apartmentHunting(blocks, reqs))