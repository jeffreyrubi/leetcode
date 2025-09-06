from src.remove_n_node_from_end_of_list import Solution, ListNode

def test_remove_n_node_from_end_of_list():
    solution = Solution()

    def build_list(values):
        head = ListNode(values[0]) if values else None
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

    # Test case 1: Remove 2nd node from end
    head = build_list([1,2,3,4,5])
    result = solution.removeNthFromEnd(head, 2)
    assert list_to_array(result) == [1,2,3,5]

    # # Test case 2: Remove only node
    head = build_list([1])
    result = solution.removeNthFromEnd(head, 1)
    assert list_to_array(result) == []

    # Test case 3: Remove head in two-node list
    head = build_list([1,2])
    result = solution.removeNthFromEnd(head, 1)
    assert list_to_array(result) == [1]

    # Test case 4: Remove head in two-node list
    head = build_list([1,2])
    result = solution.removeNthFromEnd(head, 2)
    assert list_to_array(result) == [2]

