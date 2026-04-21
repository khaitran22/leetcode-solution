import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def mergeTwoLists(list1, list2):
#     """
#         Heap structure
#     """
#     result = []
#     heapq.heapify(result)
#     if list1 != None:
#         l = list1
#         while l != None:
#             heapq.heappush(result, -l.val)
#             l = l.next

#     if list2 != None:
#         l = list2
#         while l != None:
#             heapq.heappush(result, -l.val)
#             l = l.next

#     if len(result) > 0:
#         leng = len(result)
#         curr = ListNode(-heapq.heappop(result), None)
#         for i in range(1, leng):
#             curr = ListNode(-heapq.heappop(result), curr)
#     else:
#         return None

#     return curr

def mergeTwoLists(list1, list2):
    """
        Two pointers
    """
    if list1 == None:
        return list2

    if list2 == None:
        return list1

    if list1 == None and list2 == None:
        return None

    if list1.val < list2.val:
        head = list1
        n1, n2 = list1.next, list2
    else:
        head = list2
        n1, n2 = list1, list2.next

    prev = head

    while n1 != None or n2 != None:
        if n1 != None and n2 != None:
            if n1.val < n2.val:
                prev.next = n1
                prev = n1
                n1 = n1.next
            else:
                prev.next = n2
                prev = n2
                n2 = n2.next
        else:
            while n1 != None:
                prev.next = n1
                prev = n1
                n1 = n1.next

            while n2 != None:
                prev.next = n2
                prev = n2
                n2 = n2.next

    return head


# Helper function to build a linked list from a Python list


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# Create the two linked lists
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])
head = mergeTwoLists(list1, list2)
while head != None:
    print(head.val)
    head = head.next
