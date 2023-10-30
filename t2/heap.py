class Heap:
    def __init__(self):
        self.data = []
    
    def _left_child(self,index):
        return index * 2 +1
    
    def _right_child(self,index):
        return self._left_child(index) + 1

    def _parent(self,index):
        parent = (index-1) // 2
        return parent
    
    def _swap(self,index1,index2):
        self.data[index1],self.data[index2]=self.data[index2],self.data[index1]
    def insert(self,value):
        self.data.append(value)
        current_idx = len(self.data) - 1
        while current_idx >0 and self.data[current_idx] > self.data[self._parent(current_idx)]:
            self._swap(current_idx,self._parent(current_idx))
            current_idx = self._parent(current_idx)
    def _sink_down(self,index):
        max_index = index
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            if  left< len(self.data) and  self.data[left] > self.data[max_index]:
                max_index = left
            if right < len(self.data) and self.data[right]>self.data[max_index]:
                max_index = right
            if max_index == index:
                return
            else:
                self._swap(index,max_index)
                index = max_index
        
    def remove(self):
        if len(self.data) == 0:
            return None
        if len(self.data) ==1:
            return self.data.pop()
        temp = self.data[0]
        self.data[0] = self.data.pop()
        self._sink_down(0)
        return temp
    def max(self):
        return self.data[0]

        
heap = Heap()
heap.insert(99)
heap.insert(178)
heap.insert(61)
heap.insert(58)
heap.insert(144)
heap.insert(78)
heap.insert(177)
heap.insert(4)
print(heap.max())
heap.remove()
print(heap.max())
heap.remove()
print(heap.max())
heap.remove()
print(heap.max())
heap.remove()
print(heap.max())
