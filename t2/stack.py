class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def push(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            # self.top.next = self.top
            self.top= new_node

        self.length +=1

    def pop(self):
        if self.length == 0:
            return None
        temp = self.top
         
        self.top=self.top.next
        self.length -= 1
        return temp.value

stack = Stack()
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())