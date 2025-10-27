from src.daily_temperature import Solution

def test_daily_temperature():
    solution = Solution()
    # Test case 1: Example
    assert solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]

    # Test case 2: Monotonic decreasing
    assert solution.dailyTemperatures([75,74,73,72]) == [0,0,0,0]

    # Test case 3: Single day
    assert solution.dailyTemperatures([70]) == [0]

