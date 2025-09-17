from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pt_fast = head
        pt_slow = head

        if head is None:
            return False

        while pt_fast.next is not None:
            if pt_fast.next == pt_slow:
                return True
            if pt_fast.next.next is not None:
                if pt_fast.next.next == pt_slow:
                    return True
                
                pt_fast = pt_fast.next.next
                pt_slow = pt_slow.next
            else:
                # pt_fast reached the end and no cycle is found
                return False
        return False
            


