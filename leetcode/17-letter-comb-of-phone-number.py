from typing import List

class Solution:
    board = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(prefix, next_digits):
            if next_digits == "":
                out.append(prefix)
            else:
                for d in self.board[next_digits[0]]:
                    helper(prefix+d, next_digits[1:])
        out = []
        if digits:
            helper("", digits)
        return out

if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
