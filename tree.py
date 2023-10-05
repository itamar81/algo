# License https://bit.ly/2InTS3W
# Tree_sort algorithm
# Build a BST and in order traverse.
class node():
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

    def insert2(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert2(val=val)
            else:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert2(val=val)

        else:
            self.val = val

    def insert(self,val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
def traverse(root,arr):
    if root:
        traverse(root=root.left,arr=arr)
        arr.append(root.val)
        traverse(root.right,arr)
        

def inorder(root, res):
    # Recursive travesal 
    if root:
        inorder(root.left,res)
        inorder(root.right,res) 
        res.append(root.val)

def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1,len(arr)):
        root.insert2(arr[i])
    # Traverse BST in order. 
    res = []
    traverse(root,res)
    return res

arr= [5,7,6,1,7,547,456,3547,37,48,98,66,3563,48,9,66,33,33,11,4,8,78,65,27,48,15,35,55]
print(treesort(arr))
