# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            return
        if self.head is not None:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.tail = node
            return
        if self.tail is not None:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        # Write your code here.
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev == None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if self.head == nodeToInsert and self.tail == nodeToInsert:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next == None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position is 1:
            self.setHead(nodeToInsert)
            return
        currentNode = self.head
        i = 1
        while currentNode is not None and i < position:
            currentNode = currentNode.next
            i += 1
        if currentNode is not None:
            self.insertBefore(currentNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        # Write your code here.
        currentNode = self.head
        while currentNode is not None:
            tempNode = currentNode
            currentNode = currentNode.next
            if tempNode.value == value:
                self.remove(tempNode)

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
            #node.next.prev = None
        if node == self.tail:
            self.tail = self.tail.prev
            #node.prev.next = None
        self.removeBinding(node)

    def removeBinding(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    def containsNodeWithValue(self, value):
        # Write your code here.
        currentNode = self.head
        while currentNode is not None and currentNode != value:
            currentNode = currentNode.next
        return currentNode is not None

# first = Node(1)
# second = Node(2)
# third = Node(3)
# fourth = Node(4)
# fifth = Node(5)
# sixth = Node(7)

# headSet = DoublyLinkedList()
# headSet.setHead(first)
# headSet.setTail(fifth)
# headSet.insertAfter(first, second)
# headSet.insertAfter(second, third)
# headSet.insertAfter(third, fourth)
# headSet.insertAfter(fourth, fifth)

# # headSet.remove(fifth)

# headSet.insertAtPosition(2, Node(6))

# answer = headSet.containsNodeWithValue(8)
# print(answer)


# headSet.removeNodesWithValue(6)

# answer = headSet.containsNodeWithValue(5)
# print(answer)