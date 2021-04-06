def shortenPath(path):
	# Write your code here.
	startWithSlash = path[0] == '/'
	pathArr = list(filter(isUseful, path.split('/')))	
	stack = []

	for folder in pathArr:
		if folder == '..':
			if startWithSlash and len(stack) > 0:
				stack.pop()
			if not startWithSlash:
				if len(stack) > 0 and stack[-1] != '..':
					stack.pop()
				else:
					stack.append(folder)
		else:
			stack.append(folder)
	if startWithSlash:
		if len(stack) == 0:
			return '/'
		stack = [''] + stack
	return '/'.join(stack)
	

def isUseful(s):
	if s == '.' or s == '':
		return False
	return True


print(shortenPath("/foo/../test/../test/../foo//bar/./baz"))