from src.lc75_keys_and_rooms import Solution

def test_lc75_keys_and_rooms():
    solution = Solution()

    # Test case 1: Can visit all rooms
    # rooms = [[1],[2],[3],[]]
    # Start in room 0, get key to room 1, then room 2, then room 3
    assert solution.canVisitAllRooms([[1],[2],[3],[]]) == True

    # Test case 2: Cannot visit all rooms
    # rooms = [[1,3],[3,0,1],[2],[0]]
    # Can visit rooms 0, 1, 3 but cannot reach room 2
    assert solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False

    # Test case 3: Single room
    assert solution.canVisitAllRooms([[]]) == True

    # Test case 4: Two rooms, can visit both
    assert solution.canVisitAllRooms([[1],[]]) == True

    # Test case 5: Multiple keys in first room
    assert solution.canVisitAllRooms([[1,2,3],[],[],[]]) == True

    # Test case 6: Circular references but all reachable
    assert solution.canVisitAllRooms([[1,2],[3],[3],[1,2]]) == True

    # Test case 7: Cannot reach last room
    assert solution.canVisitAllRooms([[1],[2],[],[]]) == False

    # Test case 8: Complex graph with all rooms reachable
    assert solution.canVisitAllRooms([[1,3],[2,4],[0],[4],[3,2]]) == True
