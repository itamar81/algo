class Node:
    def __init__(self,value):
        self.value = value
        self.next = None    

class Queue:
    def __init__(self):
        self.root = None
        self.last = None
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = self.last =  new_node
            return
        self.last.next= new_node
        self.last = new_node

    def pop(self):
        if self.root is None:
            return None
        temp = self.root
        self.root= self.root.next
        temp.next= None
        return temp.value

q = Queue()
q.insert(4)
q.insert(9)
q.insert(5)
q.insert(7)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
q.insert(8)
print(q.pop())
