# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
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

    #my code
    def summation(self, BinaryTree, array):
        array.append(BinaryTree.value)
        if BinaryTree.left is None and BinaryTree.right is None:
            return sum(array)
        if BinaryTree.left is not None:
            self.summation(BinaryTree.left, array)
        elif BinaryTree.right is not None:
            self.summation(BinaryTree.right, array)


def branchSums(root):
    # Write your code here.
    sums = []
    calc(root, 0, sums)
    return sums

def calc(node, runningSum, sums):
    if node is None:
        return

    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calc(node.left, newRunningSum, sums)
    calc(node.right, newRunningSum, sums)

tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
print(branchSums(tree))






# def branchSums(root):
#     # Write your code here.
#     sum = []
#     limit = float('inf')
#     i = 0
#     while i < 5:
#         ans = reacher(root,limit)
#         sum.append(ans[0])
#         limit = ans[1]
#         i += 1
#     return sum

# def reacher(root, limit):
#     currentNode = root
#     count = 0
#     sum = 0
#     while currentNode is not None:
#         print('currentNode.value = ',currentNode.value)
#         if count < limit-1:
#             count += 1
#             sum += currentNode.value
#             currentNode = currentNode.left
#         else:
#             count -= 1
#             sum += currentNode.value
#             currentNode = currentNode.right
#     limit = count - 1
#     return sum, limit
