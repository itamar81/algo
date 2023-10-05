arr = [3,2,5,6,2,4,77,34,234,11,55,75,33]
class node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,item):
        if item < self.value:
            if self.left == None:
                self.left = node(item)
            else:
                self.left.insert(item)
        else:
            if self.right == None:
                self.right = node(item)
            else:
                self.right.insert(item)


def traverse(root,res):
    if root:
        traverse(root.left,res)
        res.append(root.value)
        traverse(root.right,res)

def tree_sort(arr):
    if len(arr) == 0:
        return -1
    root = node(arr[0])
    for i in range(1,len(arr)):
        root.insert(i)
    
    a = []
    traverse(root,a)
    return a

sorted = tree_sort(arr=arr)
print(sorted)