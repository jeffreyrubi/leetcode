from src.course_schedule_ii import Solution

def test_course_schedule_ii():
    solution = Solution()
    def valid_order(order, n, prereqs):
        # empty order is only valid when no possible ordering exists
        if not order:
            return False
        if len(order) != n:
            return False
        pos = {c: i for i, c in enumerate(order)}
        for a, b in prereqs:
            # a depends on b: b must come before a
            if pos.get(b, -1) >= pos.get(a, -1):
                return False
        return True

    # Test case 1: Simple two-course chain
    res = solution.findOrder(2, [[1,0]])
    assert valid_order(res, 2, [[1,0]])

    # Test case 2: Cycle -> no possible order
    res = solution.findOrder(2, [[1,0],[0,1]])
    assert res == []

    # Test case 3: Larger DAG with multiple valid orders
    numCourses = 4
    prereqs = [[1,0],[2,0],[3,1],[3,2]]
    res = solution.findOrder(numCourses, prereqs)
    assert valid_order(res, numCourses, prereqs)
