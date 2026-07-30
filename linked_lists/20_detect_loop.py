class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(20)        
n3 = Node(30)
n4 = Node(10)
n5 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n4

head = n1

def detect_loop(head):
   
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False     
print(detect_loop(head))

