from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = ListNode()
        even_end = even_head
        root = ListNode(next=head)
        prev = root
        current = head
        i = 1
        while current:
            if i % 2 > 0:
                # Odd pos node => go next node
                prev = current
                current = current.next
            else:
                # Even pos node => take it to even
                prev.next = current.next
                even_end.next = current
                current.next = None
                even_end = current
                current = prev.next
            i += 1
        
        # Add event to the prev.next
        prev.next = even_head.next
        return root.next
                






























