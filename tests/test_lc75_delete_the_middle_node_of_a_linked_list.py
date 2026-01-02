from src.lc75_delete_the_middle_node_of_a_linked_list import Solution, ListNode

def list_to_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for el in elements:
        current.next = ListNode(el)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test_lc75_delete_the_middle_node_of_a_linked_list():
    solution = Solution()

    # Test case 1: Normal case with odd number of nodes
    head = list_to_linked_list([1, 2, 3, 4, 5])
    expected = [1, 2, 4, 5]
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == expected

    # Test case 2: Normal case with even number of nodes
    head = list_to_linked_list([1, 2, 3, 4])
    expected = [1, 2, 4]
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == expected

    # Test case 3: Single node
    head = list_to_linked_list([1])
    expected = []
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == expected

    # Test case 4: Two nodes
    head = list_to_linked_list([1, 2])
    expected = [1]
    result = solution.deleteMiddle(head)
    assert linked_list_to_list(result) == expected
