class Solution:
    def recursive(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return len(s) == 0
        if p[0] == "*":
            subs = [s[i:] for i in range(len(s)+1)]
            return any(self.isMatch(sub, p[1:]) for sub in subs)
        if len(s) == 0:
            return len(p) == 0
        if s[0] == p[0] or p[0] == "?":
            return self.isMatch(s[1:], p[1:])
        return False

    def dp(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

    def isMatch(self, s, p):
        return self.dp(s, p)
        return self.recursive(s, p)


if __name__ == "__main__":
    print(Solution().isMatch("aa", "a"))  # False
    print(Solution().isMatch("aa", "*"))  # True
    print(Solution().isMatch("cb", "?a"))  # False
    print(Solution().isMatch("adceb", "*a*b"))  # True
    print(Solution().isMatch("acdcb", "a*c?b"))  # False
    print(Solution().isMatch("", "*"))  # True
    print(Solution().isMatch("aabababbaabbbbbaab", "*****a"))  # False
