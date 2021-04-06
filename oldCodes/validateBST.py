# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    currentNode = tree
	while True:
		if currentNode is None:
			return False
		elif currentNode is not None:
			if currentNode.left is not None and currentNode.right is not None:
				if currentNode.left >= currentNode.value:
					return False
				if currentNode.right <= currentNode.value:
					return False
			if currentNode.left is None:
				if currentNode.left.left is not None or currentNode.left.right is not None:
					return False
			if currentNode.right is None:
				if currentNode.right.left is not None or currentNode.right.right is not None:
					return False

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    if tree.value is None:
		return False
	else:
		if self.left is not None:
			if self.left > self.value:
				return False
		if self.right is not None:
			if self.right < self.value:
				return False
		if self.left is None and self.right is None:
			return True
			
