from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        inverse_list = []
        # Form an inverted list
        cursor = head
        while cursor is not None:
            inverse_list.append(cursor)
            cursor = cursor.next

        cursor = head
        # Insert the inverted list until it repeats
        for i in reversed(range(len(inverse_list))):
            if inverse_list[i] == cursor or inverse_list[i] == cursor.next:
                # start to repeat. 
                break

            cache = cursor.next
            cursor.next = inverse_list[i]
            cursor.next.next = cache
            cursor = cache
        
        if len(inverse_list)%2 == 0:
            # cut after the next element
            cursor.next.next = None
        else:
            cursor.next = None

