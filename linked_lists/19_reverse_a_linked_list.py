class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3
head = n1

def print_list(head):

    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")
  

def rev_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev 

print("Original List:")
print_list(head)

new_head = rev_linked_list(head)

print("Reversed List:")
print_list(new_head)