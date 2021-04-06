def interweavingStrings(one, two, three):
    # Write your code here.
    if len(one) + len(two) != len(three):
    	return False
    
    return areInterweave(one, two, three, 0, 0)

def areInterweave(one, two, three, i, j):
	k = i + j
	if k == len(three):
		return True
	
	if i < len(one) and one[i] == three[k]:
		if areInterweave(one, two, three, i + 1, j):
			return True
		
	if j < len(two) and two[j] == three[k]:
		return areInterweave(one, two, three, i, j + 1)
	
	return False

print(interweavingStrings("algo", "yes", "yaelsgo"))