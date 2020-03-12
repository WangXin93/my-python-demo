""" https://leetcode.com/problems/sudoku-solver/

Method 1: Brute Force

Method 2: Backtracking

Divide the problem to sub-problem, e.g., divide fullfill sudoku problem to fullfill a slot at specific (r, c). Then for the sub-problem, each step  has a pattern following 3 keys of backtracking:
    1. Choice: You have decision space
    2. Constraints: The decision space are constrained
    3. Goal: Like solve a soduku problem, if satisfiy the goal, return the function else trace back to another choice.

Reference:
    * <https://www.youtube.com/watch?v=Zq4upTEaQyM>
"""

from pprint import pprint
from typing import List

class Solution(object):
    def _is_valid(self, r, c, board):
        suspect = board[r][c]
        # Row
        if suspect in [board[r][_c] for _c in range(len(board[0])) if (r, _c) != (r, c)]:
            return False
        # Col
        if suspect in [board[_r][c] for _r in range(len(board)) if (_r, c) != (r, c)]:
            return False
        # Square
        topleft_r = r // 3
        topleft_c = c // 3
        possible = [board[_r][_c] for _r in range(topleft_r*3, topleft_r*3+3) for _c in range(topleft_c*3, topleft_c*3+3) if (_r, _c) != (r, c)]
        if suspect in possible:
            return False
        return True

    def _solver(self, r, c, board):
        """ At each step (r, c), the dicision space is from 1 to 9, here valid each dicision, if is_valid, go to next step (r, c+1), else trace back to next decision.
            The base case is the c is beyond the next column and r is the last row.
        """
        # Base case
        if c == len(board[r]):
            if r == len(board)-1:
                return True
            else:
                return self._solver(r+1, 0, board)

        # Skip existing number
        if board[r][c].isnumeric():
            return self._solver(r, c+1, board)

        # Select a choice from decision from 1 to 9
        for num in range(1, 10):
            board[r][c] = str(num)
            if self._is_valid(r, c, board):
                if self._solver(r, c+1, board):
                    return True
            board[r][c] = '.'

        return False

    def solve_sudoku(self, board: List[List[str]]) -> None:
        return self._solver(0, 0, board)


def test_answer():
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    correct = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    sol.solve_sudoku(board)

if __name__ == "__main__":
    sol = Solution()
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    correct = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    for r in range(9):
        for c in range(9):
            assert sol._is_valid(r, c, correct) is True
    sol.solve_sudoku(board)
