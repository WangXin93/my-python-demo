from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out = [-1, -1]
        left, right = 0, len(nums) - 1
        # find the left most
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] == target:
            out[0] = left

        # find the right most
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        if nums[right] == target:
            out[1] = right
        return out


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
