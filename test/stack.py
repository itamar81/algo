class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        #self.root = None
        self.last = None
        self.length = 0
    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.last = new_node
        else:
            new_node.next = self.last
            self.last = new_node
        self.length += 1
    
    def to_list(self):
        arr = []
        current= self.last
        while current:
            arr.append(current.value)
            current = current.next
        return arr
    def pop(self):
        temp = self.last
        self.last = self.last.next
        temp.next = None
        self.length -= 1
        return temp.value
stack = Stack()
stack.push(3)
stack.push(4)
stack.push(7)
stack.pop()
print(stack.to_list())