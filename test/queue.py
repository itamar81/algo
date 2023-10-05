class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
    

class Queue:
    def __init__(self):
        self.root = None
        self.length = 0
        self.top = None
    def push(self,value):
        new_node = Node(value=value)
        if self.length == 0:
            self.root = new_node
            self.top = new_node
        else:
            self.top.next =new_node
            self.top = new_node
        self.length += 1

    def pop(self):
        temp = self.root 
        self.root= self.root.next
        temp.next = None
        return temp

    def to_list(self):
        arr = []
        current= self.root
        while current:
            arr.append(current.value)
            current = current.next
        return arr
    
q = Queue()
q.push(3)
q.push(4)
q.push(7)
print(q.pop())
print(q.to_list())