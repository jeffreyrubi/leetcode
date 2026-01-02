from src.lc75_asteroid_collision import Solution

def test_lc75_asteroid_collision():
    solution = Solution()

    # Test case 1: Example input
    assert solution.asteroidCollision([5, 10, -5]) == [5, 10]

    # Test case 2: All asteroids destroyed
    assert solution.asteroidCollision([8, -8]) == []

    # Test case 3: Single asteroid remains
    assert solution.asteroidCollision([10, 2, -5]) == [10]

    # Test case 4: No collisions
    assert solution.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]

    # Test case 5: Large collision chain
    assert solution.asteroidCollision([1, -2, -2, -2]) == [-2, -2, -2]

