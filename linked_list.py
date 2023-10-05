class node():
  def __init__(self,value):
    self.value = value
    self.next = None
  

  def get_next(self):
    return self.next

  def insert_after(self,value):
    if self.next is None:
      self.next = node(value)
    else:
      prev_next = self.next
      self.next = node(value)


class LinkList():
  def __init__(self,head):
    self.head = node(head)
    self.tail = self.head
    self.length = 1
  
  def print_list(self):
    tmp = self.head
    while tmp:
      print(tmp.value)
      tmp = tmp.next
  
  def get(self, index):
    if self.length == 0 or index < 0 or index>=self.length:
      return -1
    temp = self.head
    for i in range(index):
      temp = temp.next
    return temp

  def pop_first(self):
    if self.length == 0:
      return None
    
    first = self.head
    second = self.head.next
    self.head = second
    first.next = None 
    self.length -=1
    return first
  
  def append(self,value):
    t = node(value)
    self.tail.next= t
    self.length += 1
    self.tail =   t
    return True
  
  def pop(self):
    if self.length == 0:
      return None
    tmp = pre  = self.head
    while tmp.next:
      pre = tmp
      tmp = tmp.next
      
    self.tail = pre
    self.tail.next= None
    self.length -= 1
    return tmp.value
  
  def prepend(self,value):
    new_node = node(value)
    if self.head:
      new_node.next = self.head
    else:
      self.tail = new_node
    self.head = new_node
    self.length += 1
    return True
    
  def get_tail(self):
    return self.tail.value


ll = LinkList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(90)
ll.prepend(44)
ll.prepend(333)
#print(ll.pop())
print(ll.print_list())
#print(ll.get_tail())
#//print(ll.tail.value)
#//print(ll.length)
print("1 value: ",ll.get(1).value)
