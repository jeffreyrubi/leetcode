from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        new_tail = head
        new_head = head
        while new_tail.next is not None:
            moving_node = new_tail.next
            new_tail.next = new_tail.next.next
            moving_node.next = new_head
            new_head = moving_node

        return new_head