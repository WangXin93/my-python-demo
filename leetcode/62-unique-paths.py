"""
[[28, 21, 15, 10, 6, 3, 1],
 [7, 6, 5, 4, 3, 2, 1],
 [1, 1, 1, 1, 1, 1, 1]]
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0 for c in range(n)] for r in range(m)]
        for r in range(m):
            for c in range(n):
                if r == 0:
                    table[r][c] = 1
                elif c == 0:
                    table[r][c] = 1
                else:
                    table[r][c] = table[r][c-1] + table[r-1][c]
        return table[m-1][n-1]

if __name__ == "__main__":
    print(Solution().uniquePaths(3, 2))  # 3
    print(Solution().uniquePaths(7, 3))  # 28
