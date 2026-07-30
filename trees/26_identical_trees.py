class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

n11 = Node(1)
n21 = Node(2)
n31 = Node(3)
n41 = Node(4)
n51 = Node(5)
n61 = Node(6)

n11.left = n21
n11.right = n31
n21.right = n41
n21.left = n51
n31.right = n61

root1 = n11

n12 = Node(1)
n22 = Node(2)
n32 = Node(3)
n42 = Node(4)
n52 = Node(5)
n62 = Node(6)

n12.left = n22
n12.right = n32
n22.right = n42
n22.left = n52
n32.right = n62

root2 = n12

def identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is None or root2 is None:
        return False
    elif root1.data != root2.data:
        return False
    left_same = identical(root1.left,root2.left)
    right_same = identical(root1.right, root2.right)
    return left_same and right_same
print(identical(root1, root2))