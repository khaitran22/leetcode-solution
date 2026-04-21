class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow

node6 = ListNode(6)
# node5 = ListNode(5, node6)
# node4 = ListNode(4, node5)
# node3 = ListNode(3, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)

# Head of the linked list
head = node6
result = middleNode(head)
while result:
    print(result.val)
    result = result.next