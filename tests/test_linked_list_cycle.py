from src.linked_list_cycle import Solution, ListNode

def test_linked_list_cycle():
    solution = Solution()

    def build_list(values, pos=-1):
        if not values:
            return None
        nodes = [ListNode(v) for v in values]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        if pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0]

    # Test case 1: List with cycle
    head1 = build_list([3,2,0,-4], 1)
    assert solution.hasCycle(head1) == True

    # Test case 2: List without cycle
    head2 = build_list([1,2])
    assert solution.hasCycle(head2) == False

    # Test case 3: Single node, no cycle
    head3 = build_list([1])
    assert solution.hasCycle(head3) == False

