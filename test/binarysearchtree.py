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

    def _insert(self,current_node,value):
        if current_node is None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self._insert(current_node.left,value)
        if value > current_node.value:
            current_node.right = self._insert(current_node.right,value=value)
        return current_node   
    def insert(self,value):
        if self.root is None:
         self.root = Node(value)
        self._insert(self.root,value)   

    def _inorder(self,current_node,arr):
        if current_node.left:
            self._inorder(current_node.left,arr)
        arr.append(current_node.value)
        if current_node.right:
            self._inorder(current_node.right,arr)
     
    def traverse(self):
        arr = []
        self._inorder(self.root,arr)
        return arr
    

bst = BST()
bst.insert(3)
bst.insert(4)
bst.insert(90)
bst.insert(1)
bst.insert(54)
bst.insert(55)
bst.insert(56)
bst.insert(52)
print(bst.root.left)
print(bst.root.right.left)
print(bst.traverse())