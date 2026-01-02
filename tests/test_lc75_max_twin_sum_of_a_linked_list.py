from src.lc75_max_twin_sum_of_a_linked_list import Solution, ListNode

def test_lc75_max_twin_sum_of_a_linked_list():
    solution = Solution()

    # Helper function to create a linked list from a list
    def create_linked_list(values):
        dummy = ListNode(0)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Test case 1: Example input
    head = create_linked_list([5, 4, 2, 1])  # Example linked list
    expected = 6  # Expected maximum twin sum
    assert solution.pairSum(head) == expected

    # Test case 2: Edge case with minimum nodes
    head = create_linked_list([1, 2])  # Minimum valid linked list
    expected = 3  # Expected maximum twin sum
    assert solution.pairSum(head) == expected

    # Test case 3: Larger input
    head = create_linked_list([1, 100000, 100000, 1])  # Larger linked list
    expected = 200000  # Expected maximum twin sum
    assert solution.pairSum(head) == expected
