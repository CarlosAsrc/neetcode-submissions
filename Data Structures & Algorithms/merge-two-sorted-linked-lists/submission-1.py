# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1

        h = None
        if list1.val <= list2.val:
            h = list1
            list1 = list1.next
        else:
            h = list2
            list2 = list2.next
        n = h
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                n.next = list1
                list1 = list1.next
                n = n.next
            else:
                n.next = list2
                list2 = list2.next
                n = n.next
        if list1 is None:
            n.next = list2

        if list2 is None:
            n.next = list1
        return h

        