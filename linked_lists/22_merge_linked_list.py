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

n4.next = n5
n5.next = n6

l1 = n1
l2 = n4

def merge(l1,l2):
    dummy = Node(-1)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            tail = tail.next
            l1 = l1.next 
        else:
            tail.next = l2
            tail = tail.next
            l2 = l2.next 

    if l1:
        tail.next = l1
    else:
        tail.next = l2  
    return dummy.next               

result = merge(l1,l2)
current = result
while current:
    print(current.data, end= "->")        
    current = current.next
print("None")     