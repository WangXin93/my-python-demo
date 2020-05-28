"""
1, 2, 3 swap diagonal  1, 4, 7    mirror  7, 4, 1
4, 5, 6       =>       2, 5, 8      =>    8, 5, 2
7, 8, 9                3, 6, 9            9, 6, 3
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    Solution().rotate(m1)
    print(m1)
