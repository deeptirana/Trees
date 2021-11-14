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

def isfullBT(root):
    if root is None:
        return True

    #leaf node
    if root.left is None and root.right is None:
        return True  

    if root.left is not None and root.right is not None:
        return (isfullBT(root.left) and isfullBT(root.right))       

    return False    

def issymmetric(root1,root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return (issymmetric(root1.left,root2.right)and 
                    issymmetric(root1.right,root2.left))

    return False    


def vertical_order(root,v,h,map1):
    if root is  None:
        return    
    vertical_order(root.left,v+1,h-1,map1)
    if h in map1:
        map1[h].append((v,root.data))
    else:
        map1[h] = [((v,root.data))]    

    vertical_order(root.right,v+1,h+1,map1)   
    return map1

BT = Tree(1)
BTL = Tree(5)
BTR = Tree(8)
BT.left = BTL
BT.right = BTR
BTR.left = Tree(17)
BTR.right = Tree(24)
BTR.left.right = Tree(9)
BTR.left.right.left = Tree(2)
# inorder(BT)
# preorder(BT)
# postorder(BT)
# levelorder(BT)
# print(height(BT))
# print(isfullBT(BT))
# print(issymmetric(BT,BT))
h=0
v=0
map1={}
vertical_order(BT,0,0,map1)

for i in sorted(map1.keys()):
    column = [j[1] for j in sorted(map1[i])]
    print(column)
