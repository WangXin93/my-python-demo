""" Edit distance
https://leetcode.com/problems/edit-distance/
https://www.wikiwand.com/en/Levenshtein_distance
https://rosettacode.org/wiki/Levenshtein_distance
"""
from functools import wraps

def memoize(func):
    memo = {}
    @wraps(func)
    def wrapper(*args):
        try:
            return memo[args]
        except KeyError:
            rv = func(*args)
            memo[args] = rv
            return rv
    return wrapper

class Solution:
    @memoize
    def minDistanceRecursive(self, word1:str, word2:str) -> int:
        """
        >>> sol = Solution();
        >>> sol.minDistanceRecursive("horse", "ros")
        3
        >>> sol.minDistanceRecursive("intention", "execution")
        5
        """
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        if word1[-1] == word2[-1]:
            return self.minDistanceRecursive(word1[:-1], word2[:-1])
        replace = self.minDistanceRecursive(word1[:-1], word2[:-1])
        insert = self.minDistanceRecursive(word1, word2[:-1])
        delete = self.minDistanceRecursive(word1[:-1], word2)
        return 1 + min(replace, insert, delete)

    def minDistance(self, word1:str, word2:str) -> int:
        """
        >>> sol = Solution();
        >>> sol.minDistance("horse", "ros")
        3
        >>> sol.minDistance("intention", "execution")
        5
        >>> sol.minDistance("", "a")
        1
        """
        word1_len = len(word1)
        word2_len = len(word2)
        table = [[0]*(word2_len+1) for _ in range(word1_len+1)]

        for i in range(word1_len+1):
            for j in range(word2_len+1):
                if i == 0:
                    table[i][j] = j
                elif j == 0:
                    table[i][j] = i
                elif word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    insert = table[i-1][j]
                    delete = table[i][j-1]
                    replace = table[i-1][j-1]
                    table[i][j] = 1 + min(replace, insert, delete)

        return table[word1_len][word2_len]

