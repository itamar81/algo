class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self,index):
        return (index-1) // 2 

    def _swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]
    def insert(self,value):
        h = self.heap
        min_index = len(h)

        
        h.append(value)
        if min_index ==0:
            return 
        
        while (h[min_index]<h[self._parent(min_index)] and min_index >0 ):
            self._swap(min_index,self._parent(min_index))
            min_index = self._parent(min_index)
    def _left_child(self,index):
        return index *2 +1
    
    def _right_child(self,index):
        return self._left_child(index) + 1

    def _rearrange(self):
        current_index  = 0
        min_index = 0
        h = self.heap
        while True:
            left_child = self._left_child(current_index)
            right_child = self._right_child(current_index)
            if left_child > len(h) and h[min_index] > h[left_child]:
                min_index = left_child
            if right_child > len(h) and h[min_index] > h[right_child]:           
                min_index = right_child
            if min_index == current_index:
                return
            self._swap(min_index,right_child)
            current_index = min_index
            
    def pop(self):
        h = self.heap
        length = len(h)
        if length == 0:
            return -1
        first = h[0]
        h[0] = h.pop()
        self._rearrange()
        return first

heap = MinHeap()
heap.insert(99)
heap.insert(72)
heap.insert(61)
heap.insert(58)
print(heap.pop())
print(heap.pop())
print(heap.heap)