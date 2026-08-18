# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nodes = {}
        while head is not None:
            if head.val in seen_nodes:
                if seen_nodes[head.val] == head:
                    return True
            seen_nodes[head.val] = head
            head = head.next
        return False
        