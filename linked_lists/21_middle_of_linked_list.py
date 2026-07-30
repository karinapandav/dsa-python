class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(29)
n2 = Node(20)
n3 = Node(28)
n4 = Node(22)
n5 = Node(35)
n6 = Node(44)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
head = n1

def middle(head):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    return slow.data
print(middle(head))
