class Node:
    def __init__(self,value):
        self.value = value
        self.next = None    

class Queue:
    def __init__(self):
        self.length = 0
        self.root = None
        self.last = None
    def insert(self, value):
        node =Node(value)
        if self.length == 0:
            self.root = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length +=1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.root
        self.length -= 1
        self.root= self.root.next
        temp.next = None
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