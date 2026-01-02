from src.lc75_odd_even_linked_list import Solution, ListNode

def list_to_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_lc75_odd_even_linked_list():
    solution = Solution()

    # Test case 1
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [1, 3, 5, 2, 4]

    # Test case 2
    head = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == [2, 3, 6, 7, 1, 5, 4]

    # Test case 3
    head = list_to_linked_list([])
    result = solution.oddEvenList(head)
    assert linked_list_to_list(result) == []

