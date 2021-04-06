class LinkedList:
    def __init__(self, value = None, nextNode = None):
        self.value = value
        self.next = nextNode


linkedList1Head = LinkedList(2)
linkedList1N2 = LinkedList(4)
linkedList1N3 = LinkedList(3)
linkedList1N4 = LinkedList(5)


linkedList1Head.next = linkedList1N2
linkedList1N2.next = linkedList1N3
linkedList1N3.next = linkedList1N4


linkedList2Head = LinkedList(5)
linkedList2N2 = LinkedList(6)
linkedList2N3 = LinkedList(1)

linkedList2Head.next = linkedList2N2
linkedList2N2.next = linkedList2N3


def AddTwoNum(linkedList1, linkedList2):
    curOneNode = linkedList1
    curTwoNode = linkedList2

    resultList = LinkedList()
    lastNodeCarry = 0
    resultHead = resultList

    while curOneNode is not None and curTwoNode is not None:
        node1Val = curOneNode.value
        node2Val = curTwoNode.value

        curSum = node1Val + node2Val + lastNodeCarry
        
        curResult = curSum % 10 
        lastNodeCarry = curSum // 10

        if resultList.value is None:
            resultList.value = curResult
        else:
            resultList.next = LinkedList(curResult)
            resultList = resultList.next
        
        curOneNode = curOneNode.next
        curTwoNode = curTwoNode.next
    
    while curOneNode is not None:
        node1Val = curOneNode.value
        curSum = node1Val + lastNodeCarry
        
        curResult = curSum % 10 
        lastNodeCarry = curSum // 10

        resultList.next = LinkedList(curResult)
        resultList = resultList.next

        curOneNode = curOneNode.next
    
    while curTwoNode is not None:
        node1Val = curTwoNode.value
        curSum = node1Val + lastNodeCarry
        
        curResult = curSum % 10 
        lastNodeCarry = curSum // 10

        resultList.next = LinkedList(curResult)
        resultList = resultList.next

        curTwoNode = curTwoNode.next

    if lastNodeCarry != 0:
        resultList.next = LinkedList(lastNodeCarry)
    
    return resultHead

result = AddTwoNum(linkedList1Head, linkedList2Head)

curNode = result
while curNode is not None:
    print(curNode.value)
    curNode = curNode.next




    

        











