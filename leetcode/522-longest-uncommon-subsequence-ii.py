from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        maxLen = -1
        for i in range(len(strs)):
            curr = strs[i]
            rest = strs[:i] + strs[i+1:]
            if all(not self.isSubsequence(curr, r) for r in rest):
                maxLen = max(maxLen, len(curr))
        return maxLen

    def isSubsequence(self, s: str, t: str) -> bool:
        buf = list(s)
        for char in t:
            if len(buf) == 0:
                break
            if char == buf[0]:
                buf.pop(0)
        return len(buf) == 0

if __name__ == "__main__":
    print(Solution().findLUSlength(["aabbcc", "aabbcc","cb","abc"]))