class Heap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        left = index * 2 +1
        return left
    
    def _right_child(self,index):
        return self._left_child(index) + 1
    
    def _parent(self,index):
        return (index - 1) // 2
    def _swap(self,index1,index2):
        self.heap[index1] , self.heap[index2] = self.heap[index2] , self.heap[index1]
    
    def _sink_down(self,index):
        max = index
        while True:
            left_child = self._left_child(index)
            right_child = self._right_child(index)
            if (left_child <len(self.heap) and
                 self.heap[left_child] > self.heap[max]):
                max = left_child
            if (right_child < len(self.heap) and
                self.heap[right_child] > self.heap[max]):
                max = right_child
            if max != index:
                self._swap(max,index)
                index=max
            else:
                return    
                

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
    def insert(self,value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        while current_index >0 and self.heap[current_index] > self.heap[self._parent(current_index)]:
            self._swap(current_index,self._parent(current_index))
            current_index = self._parent(current_index)
    def to_list(self):
        return Heap

heap = Heap()
heap.insert(99)
heap.insert(72)
heap.insert(61)
heap.insert(58)
print(heap.heap)

heap.insert(100)
print(heap.heap)
heap.insert(75)
heap.remove()
heap.remove()
heap.remove()
print(heap.heap)


            
                

