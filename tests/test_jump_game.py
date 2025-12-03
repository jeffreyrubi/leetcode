from src.jump_game import Solution

def test_jump_game():
    solution = Solution()
    # assert solution.canJump([2,3,1,1,4]) == True
    # assert solution.canJump([3,2,1,0,4]) == False
    # assert solution.canJump([0]) == True
    # assert solution.canJump([1,2,3]) == True
    # assert solution.canJump([2,0,0]) == True
    # assert solution.canJump([1,0,0]) == False
    assert solution.canJump([5,4,3,2,1,0,0]) == True
    assert solution.canJump([1,1,1,0,2]) == False
