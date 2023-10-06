class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]
    
    def _parent(self,index):
        return (index -1 ) // 2
    
    def _left_child(self,index):
        return index * 2 + 1
    
    def _right_child(self,index):
        return self._left_child(index) + 1
    
    def insert(self,value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        while current_index > 0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
            self._swap(current_index,self._parent(current_index))
            current_index = self._parent(current_index)

    def _sink_down(self,index):
        max_index = index
        h = self.heap
        while True:
            left_child_idx = self._left_child(index)
            right_child_idx = self._right_child(index)
            if left_child_idx <len(self.heap) and h[left_child_idx] > h[max_index]:
                max_index = left_child_idx
            if right_child_idx <len(self.heap) and h[right_child_idx] > h[max_index]:
                max_index = right_child_idx

            if max_index == index:
                return
            self._swap(index,max_index)
            index = max_index


    def pop(self):
        first = self.heap[0]
        last = self.heap.pop()
        self.heap[0] = last
        self._sink_down(0)
        return first

heap = MaxHeap()
heap.insert(99)
heap.insert(72)
heap.insert(61)
heap.insert(58)
print(heap.heap)
heap.pop()
print(heap.heap)