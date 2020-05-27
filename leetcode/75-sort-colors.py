from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        p0, curr, p2 = 0, 0, len(nums)-1
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                curr += 1
                p0 += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

    # Bubble sort
    # def sortColors(self, nums: List[int]) -> None:
    #     for i in range(len(nums)-1):
    #         for j in range(0, len(nums) -i - 1):
    #             if nums[j] > nums[j+1]:
    #                 nums[j], nums[j+1] = nums[j+1], nums[j]

    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     d = [0, 0, 0]
    #     for num in nums:
    #         d[num] += 1

    #     i = 0
    #     for num in range(3):
    #         while d[num] > 0:
    #             nums[i] = num
    #             d[num] -= 1
    #             i += 1


if __name__ == "__main__":
    lst = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(lst)
    print(lst)
