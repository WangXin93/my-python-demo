from typing import List


"""
          [2, 3]
   [2]
          [2]
[]
          [3]
   []
          []

          [1, 3]
   [1]
          [1]
[1]
          [1, 2, 3]
   [1, 2]
          [1, 2]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        return res

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     lst = []
    #     def helper(depth):
    #         if depth < len(nums):
    #             lst.append(nums[depth])
    #             helper(depth+1)
    #             lst.pop(-1)
    #             helper(depth+1)
    #         if depth == len(nums):
    #             res.append(lst.copy())
    #     helper(0)
    #     return res


if __name__ == "__main__":
    print(Solution().subsets([1]))
    print(Solution().subsets([1, 2]))
    print(Solution().subsets([1, 2, 3]))
