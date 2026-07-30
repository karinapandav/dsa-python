class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3
n2.right = n4
n2.left = n5
n3.right = n6

root = n1
#plr
def preorder(root):
    if root == None:
        return 
    print(root.data)
    preorder(root.left)
    preorder(root.right)

#lpr
def inorder(root):
    if root == None:
        return 
    inorder(root.left)
    print(root.data)
    inorder(root.right)

#lrp
def postorder(root):
    if root == None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data)

print("preoder:")
preorder(root)
print("inorder:")
inorder(root) 
print("postorder:")
postorder(root)   