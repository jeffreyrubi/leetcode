from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        root = ListNode(next=head)
        parent = root
        pointer_1 = root
        pointer_2 = root
        pointer_2_count = -1

        while pointer_2.next is not None:
            parent = pointer_1
            pointer_1 = pointer_1.next
            pointer_2_count += 2 if pointer_2.next.next else 1
            pointer_2 = pointer_2.next.next if pointer_2.next.next else pointer_2.next

        if pointer_2_count%2 > 0:
            parent = parent.next
            pointer_1 = pointer_1.next
        
        parent.next = pointer_1.next
        return head
        