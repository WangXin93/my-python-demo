from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        width, height = len(board[0]), len(board)

        def dfs(r, c, word):
            if len(word) == 0 or board[r][c] == word:
                return True
            if board[r][c] != word[0]:
                return False
            visited[r][c] = True
            if r > 0 and not visited[r-1][c] and dfs(r-1, c, word[1:]):
                return True
            if c > 0 and not visited[r][c-1] and dfs(r, c-1, word[1:]):
                return True
            if r < height - 1 and not visited[r+1][c] and dfs(r+1, c, word[1:]):
                return True
            if c < width - 1 and not visited[r][c+1] and dfs(r, c+1, word[1:]):
                return True
            visited[r][c] = False
            return False

        visited = [[False for _ in range(width)] for _ in range(height)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, word):
                    return True
        return False


if __name__ == "__main__":
    board = [
      ['A','B','C','E'],
      ['S','F','C','S'],
      ['A','D','E','E']
    ]
    print(Solution().exist(board, "ABCCED"))  # True
    print(Solution().exist(board, "SEE"))  # True
    print(Solution().exist(board, "ABCB"))  # False
    board = [
        ['a', 'b'],
        ['c', 'd']
    ]
    print(Solution().exist(board, "cdba"))  # False
