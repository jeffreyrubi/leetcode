from src.merge_interval import Solution

def test_merge_interval():
    solution = Solution()
    
    # Test case 1: Basic overlapping intervals
    assert solution.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    
    # Test case 2: All intervals overlap into one
    assert solution.merge([[1,4],[4,5]]) == [[1,5]]
    
    # Test case 3: No overlapping intervals
    assert solution.merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    
    # Test case 4: Single interval
    assert solution.merge([[1,4]]) == [[1,4]]
    
    # Test case 5: Empty list
    assert solution.merge([]) == []
    
    # Test case 6: Multiple overlapping intervals that merge into one
    assert solution.merge([[1,3],[2,6],[8,10],[9,12],[15,18]]) == [[1,6],[8,12],[15,18]]
    
    # Test case 7: Intervals in random order
    assert solution.merge([[15,18],[1,3],[8,10],[2,6]]) == [[1,6],[8,10],[15,18]]
    
    # Test case 8: Adjacent intervals (touching but not overlapping)
    assert solution.merge([[1,4],[5,6]]) == [[1,4],[5,6]]
    
    # Test case 9: Intervals where one is completely inside another
    assert solution.merge([[1,10],[2,3],[4,5]]) == [[1,10]]
    
    print("All merge interval tests passed!")