class node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

def arrtoBST(nums,T):
    mid = int(len(nums)/2)
    left = nums[:mid]
    right = nums[mid+1:]

    T.val = nums[mid]
    if len(left) > 0:
        T.left = TreeNode(0)
        arrtoBST(left,T.left)

    if len(right) > 0:
        T.right = TreeNode(0)
        arrtoBST(right,T.right)

def inorder_traverse(root):
    if root != None:
        print str(root)
        inorder_traverse(root.left)
        inorder_traverse(root.right)

def construct_tree(values):
    if len(values) == 1:
        root = node(values[0])
    elif len(values) == 2:
        root = node(values[0])
        root.left = construct_tree(values[1:])
    elif len(values) > 2:
        root = node(values[0])
        l = len(values)-1
        left_values = values[1:1+l//2]
        right_values = values[1+l//2:]
        root.left = construct_tree(left_values) 
        root.right = construct_tree(right_values)
    else:
        root = None

    return root

if __name__ == '__main__':
    values = [1]*10
    root = construct_tree(values)
    inorder_traverse(root)
