def heapSort(array):
    # Write your code here.
    heap = Heap(array)
    result = []
    print(heap.heap)
    while len(heap.heap) > 0:
    	smallVal = heap.remove()
    	print(smallVal)
    	print(heap.heap)
    	result.append(smallVal)
    return result

class Heap:
	def __init__(self, array):
		self.heap = []
		self.buildHeap(array)
		
	def buildHeap(self, array):
		for i in array:
			self.insert(i)
		
	
	def insert(self, number):
		self.heap.append(number)
		self.siftUp()
	
	def remove(self):
		self.siftDown()
		return self.heap.pop()
	
	def siftDown(self):
		curIdx = 0
		childOne = (2 * curIdx) + 1
		childTwo = (2 * curIdx) + 2
		while childOne < len(self.heap):
			if childTwo < len(self.heap) and self.heap[childOne] >= self.heap[childTwo]:
				swapIdx = childTwo
			else:
				swapIdx = childOne
			self.swap(swapIdx, curIdx)
			curIdx = swapIdx
			childOne = (2 * curIdx) + 1
			childTwo = (2 * curIdx) + 2
		return
	
	def siftUp(self):
		curIdx = len(self.heap) - 1
		while curIdx > 0 and curIdx < len(self.heap):
			parentIdx = (curIdx - 1) // 2
			if self.heap[parentIdx] > self.heap[curIdx]:
				self.swap(parentIdx, curIdx)
			else:
				return
			curIdx = parentIdx
			# parentIdx = (curIdx - 1) // 2
	
	def swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

print(heapSort([8, 5, 2, 9, 5, 6, 3]))