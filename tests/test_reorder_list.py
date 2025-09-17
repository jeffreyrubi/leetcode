from src.reorder_list import Solution, ListNode

def test_reorder_list():
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

    # Test case 1: Even number of nodes
    head1 = build_list([1,2,3,4])
    solution.reorderList(head1)
    assert list_to_array(head1) == [1,4,2,3]

    # Test case 2: Odd number of nodes
    head2 = build_list([1,2,3,4,5])
    solution.reorderList(head2)
    assert list_to_array(head2) == [1,5,2,4,3]

    # Test case 3: Single node
    head3 = build_list([1])
    solution.reorderList(head3)
    assert list_to_array(head3) == [1]
