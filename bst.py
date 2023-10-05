class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
  def insert(self,new_node):
    if new_node.value >self.value:
      if self.right == None:
        self.right = new_node
      else:
        self.right.insert(new_node)
    else:
      if self.left == None:
        self.left = new_node
      else:
        self.left.insert(new_node)

class BST:
  def __init__(self):
    self.root = None

  def insert(self,value):
    new_node = Node(value)
    if self.root == None:
      self.root = new_node
      return True
    self.root.insert(new_node)

  def contains(self,value):
    if self.root == None:
      return False
    temp = self.root
    while temp:
      if temp.value >  value:
        temp = temp.left
      elif temp.value < value:
        temp =temp.right
      else:
        return True
    return False
bst = BST()
bst.insert(3)
bst.insert(2)
bst.insert(4)

bst.insert(1)
print(bst.contains(2))
print(bst.root.left.value)
