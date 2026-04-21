import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):
    result = []
    heapq.heapify(result)
    for l in lists:
        while l != None:
            heapq.heappush(result, l.val)
            l = l.next

    head = None
    while len(result) != 0:
        if head == None:
            head = ListNode(heapq.heappop(result), None)
            curr = head
        else:
            new_n = ListNode(heapq.heappop(result), None)
            curr.next = new_n
            curr = new_n

    return head


# Create nodes
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(7)
n8 = ListNode(8)
n9 = ListNode(9)
n10 = ListNode(10)

# Link them: 1 -> 2 -> ... -> 10
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10

head = n1

mergeKLists([head])
