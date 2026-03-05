from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # thoughts: Reverse nodes from position left to right in one pass
        # Time: O(n), space: O(1)
        
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        # Move prev to node before left position
        for _ in range(left - 1):
            prev = prev.next
        
        # curr is at left position, will become tail of reversed section
        curr = prev.next
        
        # Reverse nodes from left to right using insertion method
        for _ in range(right - left):
            # Remove next node and insert it after prev
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummy.next