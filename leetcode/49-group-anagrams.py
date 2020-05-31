from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def countSort(s):
            counter = [0 for _ in range(26)]
            for c in s:
                counter[ord(c) - ord('a')] += 1
            out = []
            for c in counter:
                out.append(chr(c + ord('a')))
            return ''.join(out)
        d = defaultdict(list)
        for s in strs:
            d[''.join(countSort(s))].append(s)
        return list(d.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return list(d.values())


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
