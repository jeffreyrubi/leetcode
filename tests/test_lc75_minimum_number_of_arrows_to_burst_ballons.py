from src.lc75_minimum_number_of_arrows_to_burst_ballons import Solution

def test_lc75_minimum_number_of_arrows_to_burst_ballons():
    solution = Solution()
    
    # Test case 1
    points = [[10,16],[2,8],[1,6],[7,12]]
    assert solution.findMinArrowShots(points) == 2

    # Test case 2
    points = [[1,2],[3,4],[5,6],[7,8]]
    assert solution.findMinArrowShots(points) == 4

    # Test case 3
    points = [[1,2],[2,3],[3,4],[4,5]]
    assert solution.findMinArrowShots(points) == 2

    # Test case 4
    points = [[1,10],[2,3],[4,5],[6,7],[8,9]]
    assert solution.findMinArrowShots(points) == 4

    # Test case 5
    points = []
    assert solution.findMinArrowShots(points) == 0
