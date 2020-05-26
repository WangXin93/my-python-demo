from typing import List


class Solution:
    def merge(
            self, nums1: List[int],
            m: int, nums2: List[int],
            n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m-1
        i2 = n-1
        for i in range(m+n-1, -1, -1):
            if i2 < 0:
                return
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1

        # i1 = 0
        # i2 = 0
        # replaced = []
        # for i in range(m+n):
        #     if i1 == m:
        #         nums1[i] = nums2[i2]
        #         i2 += 1
        #     elif i2 == n:
        #         replaced.append(nums1[i])
        #         nums1[i] = replaced.pop(0)
        #     elif replaced and replaced[0] <= nums2[i2]:
        #         replaced.append(nums1[i])
        #         nums1[i] = replaced.pop(0)
        #         i1 += 1
        #     elif replaced and replaced[0] > nums2[i2]:
        #         replaced.append(nums1[i])
        #         nums1[i] = nums2[i2]
        #         i2 += 1
        #     elif nums1[i] >= nums2[i2]:
        #         replaced.append(nums1[i])
        #         nums1[i] = nums2[i2]
        #         i2 += 1
        #     elif nums1[i] < nums2[i2]:
        #         i1 += 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
