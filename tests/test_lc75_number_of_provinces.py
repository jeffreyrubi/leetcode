from src.lc75_number_of_provinces import Solution

def test_lc75_number_of_provinces():
    solution = Solution()

    # Test case 1: Example from LeetCode - 2 provinces
    isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
    assert solution.findCircleNum(isConnected1) == 2

    # Test case 2: Example from LeetCode - 3 provinces
    isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
    assert solution.findCircleNum(isConnected2) == 3

    # Test case 3: Single city
    isConnected3 = [[1]]
    assert solution.findCircleNum(isConnected3) == 1

    # Test case 4: All cities connected
    isConnected4 = [[1,1,1],[1,1,1],[1,1,1]]
    assert solution.findCircleNum(isConnected4) == 1

    # Test case 5: 4 cities with 2 provinces
    isConnected5 = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
    assert solution.findCircleNum(isConnected5) == 2

    # Test case 6: 5 cities with complex connections
    isConnected6 = [[1,0,0,1,0],[0,1,1,0,0],[0,1,1,0,0],[1,0,0,1,0],[0,0,0,0,1]]
    assert solution.findCircleNum(isConnected6) == 3

    # Test case 7: Linear chain
    isConnected7 = [[1,1,0],[1,1,1],[0,1,1]]
    assert solution.findCircleNum(isConnected7) == 1

    isConnected8 = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    assert solution.findCircleNum(isConnected8) == 1
