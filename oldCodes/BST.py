# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True
        elif value <= self.value:
            if self.left is None:
                return False
            else:
                if self.left == value:
                    return True
                else:
                    return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                if self.right == value:
                    return True
                else:
                    return self.right.contains(value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self.value == value:
            if self.right is not None:
                myresult = self.right.removeHelper()
                self.value = myresult
                self.right.remove(value)
            elif self.left is not None:
                myresult = self.left.removeHelper()
                self.value = myresult
                self.left.remove(value)
            else:
                self.value = None
        elif self.value < value:
            self.right.remove(value)
        else:
            self.left.remove(value)
        return self

    def removeHelper(self):
        if self.left is not None:
            return self.left.removeHelper()
        else:
            return self.value

test4 = (
    BST(10)
    .insert(5)
    .insert(15)
    .insert(22)
    .insert(17)
    .insert(34)
    .insert(7)
    .insert(2)
    .insert(5)
    .insert(1)
    .insert(35)
    .insert(27)
    .insert(16)
    .insert(30)
    .remove(22)
    .remove(17)
)