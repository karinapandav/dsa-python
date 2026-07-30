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

def ht(root):
    if root is None:
        return 0
    else:
        left = ht(root.left)
        right = ht(root.right)
        return 1 + max(left,right)
print(ht(root))    