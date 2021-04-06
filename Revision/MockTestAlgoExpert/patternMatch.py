def globMatching(fileName, pattern):
    # Write your code here.
    if len(pattern) == 0:
    	return False
    elif len(pattern) == 1:
    	if pattern == '*':
    		return True
    	elif len(fileName) == 1:
    		return True
    	else:
    		return False

    i = 0
    j = 0
    expectedNextChar = None

    while j < len(fileName) and i < len(pattern):
    	if pattern[i] == fileName[j]:
    		i += 1
    		j += 1
    		continue
        
    	elif pattern[i] == '?':
    		i += 1
    		j += 1
    		continue    
    	if pattern[i] == '*':
    		if i + 1 < len(pattern):
    			expectedNextChar = pattern[i + 1]
    			j += 1
    		else:
    			return True
    
    	if expectedNextChar is not None and expectedNextChar == fileName[j]:
    		expectedNextChar = None
    		i += 1
    
    
    if i == len(pattern) and j == len(fileName):
    	return True
    else:
    	return False


print(globMatching("abcdeflg","a*e??g"))