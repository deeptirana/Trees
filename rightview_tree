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



n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)

n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right = Node(7)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

main_right(root)



