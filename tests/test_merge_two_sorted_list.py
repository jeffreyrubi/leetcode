from src.merge_two_sorted_list import Solution, ListNode

def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def list_to_array(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

def test_merge_two_sorted_list():
    solution = Solution()

    # Test case 1: Merge two non-empty lists
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    result = solution.mergeTwoLists(l1, l2)
    assert list_to_array(result) == [1,1,2,3,4,4]

    # Test case 2: Merge with one empty list
    l1 = build_list([])
    l2 = build_list([0])
    result = solution.mergeTwoLists(l1, l2)
    assert list_to_array(result) == [0]

    # Test case 3: Merge two empty lists
    l1 = build_list([])
    l2 = build_list([])
    result = solution.mergeTwoLists(l1, l2)
    assert list_to_array(result) == []