from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        firstColZero = False
        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                firstRowZero = True
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                firstColZero = True
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if firstRowZero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if firstColZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    print(matrix)
    matrix = [[0, 1]]
    Solution().setZeroes(matrix)
    print(matrix)
    matrix = [[1, 1, 1], [0, 1, 2]]
    Solution().setZeroes(matrix)
    print(matrix)
