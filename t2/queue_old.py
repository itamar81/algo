class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
       

class Queue:
    def __init__(self):
        self.root = None
        self.last = None
        self.length = 0
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.root = new_node
            self.last = new_node
        self.last.next = new_node
        self.last = new_node
        self.length += 1
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.root 
        self.root = self.root.next
        self.length -= 1
        return temp.value


q = Queue()
q.enqueue(4)
q.enqueue(3)
q.enqueue(9)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(8)
print(q.dequeue())