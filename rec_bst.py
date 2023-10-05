class Node:
  def __init__(self,value):
    self.value = value
    self.left = None
    self.right = None

  def __str__(self):
    return str(self.value)
class BST:
  def __init__(self):
    self.root = None
  
  def __insert(self,current_node,value):
    if current_node is None:
      return Node(value)
    if value < current_node.value:
      current_node.left = self.__insert(current_node.left,value)  
    else:
      current_node.right = self.__insert(current_node.right,value)
    return current_node
  def insert(self,value):
    # new_node = Node(value)
    if self.root is None:
      self.root = Node(value)
      return
    self.__insert(self.root,value)
  
  def __r_contains(self,curr,value):
    if curr is None:
      return False
    if curr.value == value:
      return True
    if value < curr.value:
      return self.__r_contains(curr.left,value)
    elif value > curr.value:
      return self.__r_contains(curr.right,value)
    
  def contains(self,value):
    if self.root is None:
      return False
    return self.__r_contains(self.root,value)
  
  def __is_a_leaf(self,current_node):
    return current_node.left is None and current_node.right is None

  def __delete_node(self,current_node,value):
    if current_node is None:
      return None
    if value < current_node.value:
      current_node.left = self.__delete_node(current_node.left,value)
    if  value > current_node.value:
      right = self.__delete_node(current_node.right,value)
      current_node.right =  right
    else:
      if current_node.left == None and current_node.right == None:
        return None
      if self.__is_a_leaf(current_node.right):
        return None

  def delete_node(self,value):
    if self.root is None:
      return False
    return self.__delete_node(self.root,value)
 
 
  def __in_order(self,current_node,results):
    if current_node.left:
      self.__in_order(current_node.left,results=results)
    results.append(current_node.value)
    if current_node.right:
      self.__in_order(current_node.right,results=results)
 
 
  def traverse(self):
    current_node = self.root
    results = []
    #results.append(current_node.value)
    self.__in_order(current_node,results)
    return results

bst = BST()

bst.insert(5)
bst.insert(3)
bst.insert(1)
bst.insert(66)
bst.insert(8)
bst.insert(2)
bst.insert(79)
bst.insert(4)
bst.insert(9)
bst.insert(78)
#bst.delete_node(3)
#print(bst.contains(3))
#print(bst.contains(5))
#print(bst.root)
#print(bst.root.right)
print(bst.traverse())

    
