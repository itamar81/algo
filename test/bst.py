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
    
    def __contains(self,current_node,value):
        if current_node == None:
            return False
        if value < current_node.value:
            return self.__contains(current_node=current_node.left,value=value)
        elif value > current_node.value:
            return self.__contains(current_node.right,value=value)
        else:
            return True
    def contains(self,value):
        if self.root :
            return self.__contains(self.root,value)
        return False
    def __insert(self,current_node,value):
        if current_node is None:
            current_node = Node(value)
        if value < current_node.value:
            current_node.left = self.__insert(current_node=current_node.left,value=value)
        elif value > current_node.value:
            current_node.right = self.__insert(current_node=current_node.right,value=value)
        return current_node
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value=value)
            return
        self.__insert(self.root,value=value)

    def __in_order(self,current_node,arr):
        if current_node is None:
            return None
        self.__in_order(current_node=current_node.left,arr=arr)
        arr.append(current_node.value)
        self.__in_order(current_node=current_node.right,arr=arr)
        return arr
    def traverse(self):
        arr = []
        return self.__in_order(self.root,arr=arr)


bst = BST()
bst.insert(3)
bst.insert(5)
bst.insert(2)
bst.insert(9)
print(bst.contains(9))
print(bst.contains(3))
print(bst.contains(5))
print(bst.contains(2))
print(bst.contains(6))
print(bst.contains(8))
print(bst.traverse())