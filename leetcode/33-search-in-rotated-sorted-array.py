from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:  # if left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # if right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     offset = len(nums) - 1
    #     while offset > 0:
    #         if nums[offset] < nums[offset-1]:
    #             break
    #         offset -= 1

    #     l, r = 0, len(nums) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         midRotated = mid + offset
    #         if midRotated >= len(nums):
    #             midRotated -= len(nums)
    #         if nums[midRotated] == target:
    #             return midRotated
    #         elif nums[midRotated] > target:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return -1


if __name__ == "__main__":
    print(Solution().search([4,5,6,7,0,1,2], 0))
    print(Solution().search([4,5,6,7,0,1,2], 3))
    print(Solution().search([3, 1], 1))
