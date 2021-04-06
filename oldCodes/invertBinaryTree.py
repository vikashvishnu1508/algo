def invertBinaryTree(tree):
    # Write your code here.
    # currentNode = tree
    tree.left, tree.right = tree.right, tree.left
    if tree.left is not None and tree.right is not None:
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    elif tree.left is not None and tree.right is None:
        # tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.right)
    elif tree.left is None and tree.right is not None:
        # tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
    else:
        return tree




class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self



test2 = BinaryTree(1).insert([2])
invertBinaryTree(test2)
print(test2)
