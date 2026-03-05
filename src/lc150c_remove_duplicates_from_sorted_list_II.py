from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Remove ALL nodes that have duplicates (keep only distinct values)
        # Time: O(n), Space: O(1)
        
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # If current node has duplicates, skip all nodes with same value
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip the last duplicate too
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        
        return dummy.next