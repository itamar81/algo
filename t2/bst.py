class Node:
    def __init__(self,value):
        self.value = value
        self.left= None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def _recursive_insert(self,current_node,new_node):
        if current_node is None:
            return new_node
        if  new_node.value<current_node.value:
            current_node.left =  self._recursive_insert(current_node.left,new_node)
        else:
            current_node.right =  self._recursive_insert(current_node.right,new_node)
        return current_node

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        self._recursive_insert(self.root,new_node)

    def _inorder(self,node,arr):
        if node.left is not None:
            self._inorder(node.left,arr)
        arr.append(node.value)
        if node.right:
            self._inorder(node.right,arr)
        return arr

    def traverse(self):
        if self.root == None:
            return None
        arr = []
        return self._inorder(self.root,arr)
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