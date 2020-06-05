""" 39 Combination Sum

When you see the request for unique combinations, think about sort
the candidates firstly.
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        out = []
        seq = []
        def dfs(i, target):
            seq.append(nums[i])
            if target == 0:
                out.append(seq.copy())
            for ni in range(i, len(nums)):
                if nums[ni] <= target:
                    dfs(ni, target - nums[ni])
                else:
                    break
            seq.pop(-1)
        for i in range(len(nums)):
            dfs(i, target - nums[i])
        return out


if __name__ == "__main__":
    print(Solution().combinationSum([2, 3, 6, 7], 7))
