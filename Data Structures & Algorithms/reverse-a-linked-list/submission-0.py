# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        prev = None
        n = current.next
        while current is not None:
            n = current.next
            current.next = prev
            prev = current
            current = n
        head = prev
        return head

            

            


        