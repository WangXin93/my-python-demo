""" https://leetcode.com/problems/longest-palindromic-substring

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass



if __name__ == "__main__":
    sol = Solution()
    # out = sol.longestPalindrome('babad')
    # assert out == "bab"
    # out = sol.longestPalindrome('cbbd')
    # assert out == "bb"
    # out = sol.longestPalindrome('ccc')
    # assert out == "ccc"
    out = sol.longestPalindrome('bananas')
    assert out == "anana"
