from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, num in enumerate(nums[:-2]):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right, twosum = i+1, len(nums)-1, -num
            while left < right:
                if nums[left] + nums[right] == twosum:
                    out.append([num, nums[left], nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] > twosum:
                    right -= 1
                elif nums[left] + nums[right] < twosum:
                    left += 1
        return out


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4])) # [[-1, 1, 2], [-1, 1, -1]]
    print(Solution().threeSum([0, 0, 0])) # [0, 0, 0]
    print(Solution().threeSum([1,2,-2,-1])) # []
