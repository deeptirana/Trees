class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)           

def preorder(root):
    if root is None:
        return
    print(root.data)
    inorder(root.left)
    inorder(root.right)       

def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)   
    print(root.data)    

def levelorder(root):
    q = []
    q.append(root)

    while q:
        root = q[0]
        print(root.data)
        q.pop(0)
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)    

def height(root):
    if root is None:
        return 0

    return max(height(root.left),height(root.right)) +1 


BT = Tree('Drinks')
BTL = Tree('HOT')
BTR = Tree('Cold')
BTLL = Tree('mocha')
BTLLL = Tree('yummy')
BTLR = Tree('chai')
BTRR = Tree('frappe')
BT.left = BTL
BT.right = BTR 
BT.left.left = BTLL
BT.left.right = BTLR
BTLL.left = BTLLL
BTR.right = BTRR
# inorder(BT)
# preorder(BT)
# postorder(BT)
# levelorder(BT)
print(height(BT))
