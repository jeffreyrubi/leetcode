from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        double_list = deque()
        current = head
        while current:
            double_list.append(current)
            current = current.next

        max_value = 0
        while double_list:
            left = double_list.popleft()
            right = double_list.pop()

            max_value = max(max_value, left.val + right.val)

        return max_value