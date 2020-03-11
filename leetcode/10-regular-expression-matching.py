""" https://leetcode.com/problems/regular-expression-matching/
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            return not len(s)
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def dp_isMatch(self, s, p):
        mem = {}
        def _dp(s, p):
            if (s, p) not in mem:
                if len(p) == 0:
                    mem[(s, p)] = not len(s)
                else:
                    first_match = bool(s) and p[0] in {s[0], '.'}
                    if len(p) > 1 and p[1] == "*":
                        mem[(s, p)] = _dp(s, p[2:]) or (first_match and _dp(s[1:], p))
                    else:
                        return first_match and _dp(s[1:], p[1:])
            return mem[(s, p)]
        return _dp(s, p)


def test_answer():
    sol = Solution()
    assert sol.isMatch(s="a", p="a*") is True
    assert sol.dp_isMatch(s="a", p="a*") is True
