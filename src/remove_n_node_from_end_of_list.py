from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        i = 0
        origin = head
        new_head = head

        while head:
            if i > n:
                new_head = new_head.next
            i += 1
            head = head.next

        # remove the nth node if exist
        if new_head.next:
            if i > n:
                new_head.next = (new_head.next).next
            else:
                origin = origin.next
        else:
            origin = None
        return origin