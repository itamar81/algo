class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root= None
    
    def _rec_insert(self,current,new_node):
        if current is None:
            return new_node
        if new_node.value < current.value:
            current.left = self._rec_insert(current.left,new_node)
        else:
            current.right = self._rec_insert(current.right,new_node)
        
        return current
    def insert(self,value):
        new_node=Node(value)
        if self.root == None:
            self.root = new_node
            return
        current = self.root
        self._rec_insert(current,new_node)
    def _inorder(self,node,arr):
        if node.left is not None:
            self._inorder(node.left,arr)
        arr.append(node.value)
        if node.right is not None:
            self._inorder(node.right,arr)
        return arr


    def traverse(self):
        root = self.root
        arr = []
        if root is None:
            return None
        return self._inorder(root,arr)



bst = Tree()

bst.insert(5)
bst.insert(3)
bst.insert(1)
bst.insert(66)
bst.insert(8)
bst.insert(2)
bst.insert(79)
bst.insert(4)
bst.insert(4)
bst.insert(9)
bst.insert(78)

print(bst.traverse())