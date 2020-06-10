from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        start, bestStart, bestEnd = 0, 0, 0
        for end, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            if not missing:
                while start < end and need[s[start]] < 0:
                    need[s[start]] += 1
                    start += 1
                if bestEnd == 0 or end - start <= bestEnd - bestStart:
                    bestStart, bestEnd = start, end
        return s[bestStart:bestEnd]


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    print(Solution().minWindow(S, T))
    S = "a"
    T = "aa"
    print(Solution().minWindow(S, T))
    S = "cabwefgewcwaefgcf"
    T = "cae"
    print(Solution().minWindow(S, T))
