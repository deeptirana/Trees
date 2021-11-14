class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def rightview(root,level,max_level):
    if root is None:
        return
    if max_level[0]<level:
        print(root.data)
        max_level[0] = level
    rightview(root.right,level+1,max_level)
    rightview(root.left,level+1,max_level)    


def main_right(root):
    max_level = [0]
    rightview(root,1,max_level)

def kth_dist(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
    kth_dist(root.left,k-1)    
    kth_dist(root.right,k-1)

def height(root):
    if root is None:
        return 0
    return 1+ max(height(root.left),height(root.right))

def getwidth(root,level):
    if root is None:
        return 0    
    if level==1:
        return 1
    elif level>1:
        return (getwidth(root.left, level-1)+getwidth(root.right,level-1))    

def getMaxwidth(root):
    maxwidth= 0
    h= height(root)
    for i in range(1,h+1):
        width = getwidth(root,i)
        print(width,maxwidth,h)
        if (width>maxwidth):
            maxwidth = width
    return maxwidth            
        
def diameter_BT(root):
    if root is None:
        return 0
    h1 = height(root.left)
    h2 = height(root.right)
    # print(h1,h2)
    opt1 = h1+h2+1
    opt2 = diameter_BT(root.left)
    opt3 = diameter_BT(root.right)

    return max(opt1,opt2,opt3)





# n1 = Node(1)
# n1.left = Node(2)
# n1.right = Node(3)
# n1.left.left = Node(4)
# n1.left.right = Node(5)
# n1.right.left = Node(6)
# n1.left.right.left = Node(7)
# n1.left.right.right = Node(8)

# n2 = Node(1)
# n2.left = Node(3)
# n2.right = Node(2)
# n2.right.left = Node(4)
# n2.right.right = Node(5)
# n2.left.right = Node(6)
# n2.right.right.left = Node(8)
# n2.right.right.right = Node(7)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# # main_right(root)
# kth_dist(root,2)
#print(height(root))
# getMaxwidth(root)

print(diameter_BT(root))



