""" https://leetcode.com/problems/longest-palindromic-substring

"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalindrome = ""
        for i in range(len(s)):
            # print("{}: {}".format(i, maxPalindrome))
            left, right = i, i
            while left>=1 and right<=len(s)-2 and self.isPanlindrome(s[left-1:right+2]):
                left -= 1
                right += 1
            if len(s[left:right+1]) > len(maxPalindrome): maxPalindrome = s[left:right+1]

            left, right = i, i+1
            while left >=1 and right<=len(s)-2 and self.isPanlindrome(s[left-1:right+2]):
                left -= 1
                right += 1
            if self.isPanlindrome(s[left:right+1]):
                if len(s[left:right+1]) > len(maxPalindrome): maxPalindrome = s[left:right+1]

            left, right = i-1, i
            while left >= 1 and right < len(s)-2 and self.isPanlindrome(s[left-1:right+2]):
                left -= 1
                right += 1
            if self.isPanlindrome(s[left:right+1]):
                if len(s[left:right+1]) > len(maxPalindrome): maxPalindrome = s[left:right+1]
        return maxPalindrome

    def isPanlindrome(self, s):
        return s == s[::-1]



if __name__ == "__main__":
    sol = Solution()
    out = sol.longestPalindrome('babad')
    assert out == "bab"
    out = sol.longestPalindrome('cbbd')
    assert out == "bb"
    out = sol.longestPalindrome('ccc')
    assert out == "ccc"
    out = sol.longestPalindrome('bananas')
    assert out == "anana"
