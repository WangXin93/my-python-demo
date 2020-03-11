""" https://leetcode.com/problems/maximum-subarray/

Method 1: Brute Force

Method 2: Kadane's Algorithm

Method 3: Divide & Conquer
"""

from typing import List
from itertools import accumulate

class Solution(object):
    def max_subarray(self, nums: List[int]) -> int:
        return self.dc_max_subarray(nums)

    def dc_max_subarray(self, nums):
        """ Divide and conquer
        Reference:
          * <https://www.youtube.com/watch?v=yBCzO0FpsVc>
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            L = nums[:len(nums)//2]
            R = nums[len(nums)//2:]
            l_sub = self.dc_max_subarray(L)
            r_sub = self.dc_max_subarray(R)
            c_sub = max(accumulate(L[::-1])) + max(accumulate(R))
            return max(l_sub, r_sub, c_sub)

    def kadane_max_subarray(self, nums):
        """
        https://www.youtube.com/watch?v=86CQq3pKSUw
        """
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum+num, num)
            max_sum = max(cur_sum, max_sum)
        return max_sum

    def bf_max_subarray(self, nums):
        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                max_sum = max(max_sum, sum(nums[i:j]))
        return max_sum

def test_answer():
    sol = Solution()
    assert sol.dc_max_subarray([-1, 3, 4, -5, 9, -2]) == 11
    assert sol.kadane_max_subarray([-1, 3, 4, -5, 9, -2]) == 11
    assert sol.bf_max_subarray([-1, 3, 4, -5, 9, -2]) == 11
