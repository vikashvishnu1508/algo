# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    start = head
    end = head
    i = 0
    while end.next is not None:
        end = end.next
        i += 1
        if i <= k:
            continue
        else:
            start = start.next
    if i >= k:
        start.next = start.next.next
    else:
        head.value = head.next.value
        head.next = head.next.next
    return head

test1 = LinkedList(0).addMany([1, 2, 3, 4, 5, 6, 7, 8, 9])
test1 = removeKthNodeFromEnd(test1, 10)
print(test1)
while test1.next is not None:
    print(test1.value)
    test1 = test1.next