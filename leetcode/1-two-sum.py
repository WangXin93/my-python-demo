from typing import List
from itertools import combinations


class Solution:
    # Brute force O(N^2)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for comb in combinations(range(len(nums)), 2):
    #         if nums[comb[0]] + nums[comb[1]] == target:
    #             return list(comb)

    # bi-directional search O(N logN + N + N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {num: i for i, num in enumerate(nums)}
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [idx[nums[left]], idx[nums[right]]]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1


if __name__ == "__main__":
    # print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum([3,2,4], 6))
