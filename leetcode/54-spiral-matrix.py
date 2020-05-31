"""
[[1,  2,  3,  4,  5],
 [6,  7,  8.  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
 [21, 22, 23, 24, 25]]
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        if len(matrix) == 0:
            return out
        m, n = len(matrix), len(matrix[0])
        rowBeg, rowEnd, colBeg, colEnd = 0, m-1, 0, n-1
        while (rowBeg <= rowEnd and colBeg <= colEnd):
            for i in range(colBeg, colEnd+1):
                out.append(matrix[rowBeg][i])
            rowBeg += 1
            for i in range(rowBeg, rowEnd+1):
                out.append(matrix[i][colEnd])
            colEnd -= 1
            if rowBeg <= rowEnd:
                for i in range(colEnd, colBeg-1, -1):
                    out.append(matrix[rowEnd][i])
            rowEnd -= 1
            if colBeg <= colEnd:
                for i in range(rowEnd, rowBeg-1, -1):
                    out.append(matrix[i][colBeg])
            colBeg += 1
        return out


    def spiralOrder3(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        upLeft, upRight, lowRight, lowLeft = \
            [1, 0], [0, n-1], [m-1, n-1], [m-1, 0]
        corners = [upRight, lowRight, lowLeft, upLeft]
        cornersDeltas = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
        p = [0, 0]
        out = []
        for step in range(m * n):
            out.append(matrix[p[0]][p[1]])
            if p == corners[0]:
                # Change direction
                popDir = dirs.pop(0)
                dirs.append(popDir)
                # Change corner
                popCor = corners.pop(0)
                delta = cornersDeltas.pop(0)
                cornersDeltas.append(delta)
                popCor[0], popCor[1] = \
                    popCor[0]+delta[0], popCor[1]+delta[1]
                corners.append(popCor)
            p[0], p[1] = p[0] + dirs[0][0], p[1] + dirs[0][1]
        return out


if __name__ == "__main__":
    matrix = [[]]
    print(Solution().spiralOrder(matrix))
    matrix = [[1]]
    print(Solution().spiralOrder(matrix))
    matrix = [[1, 2], [3, 4]]
    print(Solution().spiralOrder(matrix))
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
