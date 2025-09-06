from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.optimize(list1, list2)
    
    def optimize(self,list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = head = ListNode(0, None)

        while list1 or list2:
            if list1 is None:
                merged_list.next = list2
                merged_list = merged_list.next
                list2 = list2.next
            elif list2 is None:
                merged_list.next = list1
                merged_list = merged_list.next
                list1 = list1.next                   
            elif list1.val <= list2.val:
                merged_list.next = list1
                merged_list = merged_list.next
                list1 = list1.next
            elif list1.val > list2.val:
                merged_list.next = list2
                merged_list = merged_list.next
                list2 = list2.next

        return head.next


    def trial(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cursor_1 = list1
        cursor_2 = list2
        merged_list = ListNode(0, None)
        head = merged_list

        while cursor_1 is not None or cursor_2 is not None:
            if cursor_1 is None and cursor_2 is not None:
                merged_list.next = cursor_2
                cursor_2 = cursor_2.next
            elif cursor_2 is None and cursor_1 is not None:
                merged_list.next = cursor_1
                cursor_1 = cursor_1.next
            elif cursor_1.val <= cursor_2.val:
                merged_list.next = cursor_1
                cursor_1 = cursor_1.next
            else:
                merged_list.next = cursor_2
                cursor_2 = cursor_2.next
            merged_list = merged_list.next
        
        return head.next
