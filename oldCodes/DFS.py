# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
        
        #ignore this


root = Node("A")
root.addChild("B").addChild("C").addChild("D")
root.children[0].addChild("E").addChild("F")
root.children[2].addChild("G").addChild("H")
root.children[0].children[1].addChild("I").addChild("J")
root.children[2].children[0].addChild("K")

print(root.depthFirstSearch([]))