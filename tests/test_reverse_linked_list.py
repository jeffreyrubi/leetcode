from src.reverse_linked_list import Solution, ListNode


def test_reverse_linked_list():
    solution = Solution()

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

    # Test case 1: Multiple nodes
    head1 = build_list([1,2,3,4,5])
    result1 = solution.reverseList(head1)
    assert list_to_array(result1) == [5,4,3,2,1]

    # Test case 2: Single node
    head2 = build_list([1])
    result2 = solution.reverseList(head2)
    assert list_to_array(result2) == [1]

    # Test case 3: Empty list
    head3 = build_list([])
    result3 = solution.reverseList(head3)
    assert list_to_array(result3) == []
