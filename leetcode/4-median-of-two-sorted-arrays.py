""" https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

from typing import List

class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """ Set two pointer, get rid of min of two arrays each step.

            [1, 2]    [_, 2]
             ^     =>     ^
            [3, 4]    [3, 4]
             ^         ^

        """
        step = 0
        median_p = (len(nums1) + len(nums2) - 1) / 2
        median = []
        while True:
            if step - median_p >= 1:
                break
            if abs(step - median_p) <= 0.5:
                if len(nums1) == 0:
                    median.append(nums2[0])
                elif len(nums2) == 0:
                    median.append(nums1[0])
                else:
                    median.append(min(nums1[0], nums2[0]))
            if len(nums2) == 0:
                nums1 = nums1[1:]
            elif len(nums1) == 0:
                nums2 = nums2[1:]
            elif nums1[0] > nums2[0]:
                nums2 = nums2[1:]
            elif nums1[0] <= nums2[0]:
                nums1 = nums1[1:]
            step += 1
        return sum(median) / len(median)

    def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
        """ Step 4 pointer, get rid of a min and a max of two arrays each step.

            [1, 2]    [_, 2]
             ^  ^  =>     ^
            [3, 4]    [3, _]
             ^  ^      ^

        """
        len_sum = len(nums1) + len(nums2)
        steps = len_sum // 2 if len_sum % 2 else len_sum // 2 - 1
        for step in range(steps):
            # Get rid of a minimium
            if len(nums1) == 0:
                nums2 = nums2[1:]
            elif len(nums2) == 0:
                nums1 = nums1[1:]
            elif nums1[0] <= nums2[0]:
                nums1 = nums1[1:]
            elif nums1[0] > nums2[0]:
                nums2 = nums2[1:]
            # Get rid of a maximum
            if len(nums1) == 0:
                nums2 = nums2[:-1]
            elif len(nums2) == 0:
                nums1 = nums1[:-1]
            elif nums1[-1] <= nums2[-1]:
                nums2 = nums2[:-1]
            elif nums1[-1] > nums2[-1]:
                nums1 = nums1[:-1]
        median = nums1 + nums2

        median = sum(median) / len(median)
        return median

def test_answer():
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    assert sol.findMedianSortedArrays(nums1, nums2) == 2.0
    nums1 = [1, 2]
    nums2 = [3, 4]
    assert sol.findMedianSortedArrays(nums1, nums2) == 2.5

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    out = sol.findMedianSortedArrays_2(nums1, nums2)
