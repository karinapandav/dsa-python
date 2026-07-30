class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(12)
n3 = Node(15)
n4 = Node(11)
n5 = Node(13)
n6 = Node(14)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

head = n1

def remove_Nth_node(head,n):
    dummy = Node(-1)
    dummy.next = head
    fast = dummy 
    slow = dummy
    for i in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    if fast.next == None:
        slow.next = slow.next.next
    return dummy.next
result = remove_Nth_node(head,2)
current = result
while current:
    print(current.data, end='->')
    current = current.next
print("None")            