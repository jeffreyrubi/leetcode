from src.course_schedule import Solution

def test_course_schedule():
    solution = Solution()

    # Test case 1: Possible to finish all courses
    assert solution.canFinish(2, [[1,0]]) == True

    # Test case 2: Impossible to finish due to cycle
    assert solution.canFinish(2, [[1,0],[0,1]]) == False

    # Test case 3: Multiple courses, possible
    assert solution.canFinish(4, [[1,0],[2,1],[3,2]]) == True

