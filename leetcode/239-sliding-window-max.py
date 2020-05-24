"""
monotonic deque techique
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        maxs = []
        for i in range(len(nums)):
            if i >= k and q[0] == nums[i-k]:
                q.popleft()
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            if i >= k-1:
                maxs.append(q[0])
        return maxs

    # Another version
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     q = deque()
    #     maxs = []
    #     for i in range(len(nums)):
    #         if q and q[0] < i-k+1:
    #             q.popleft()
    #         while q and nums[q[-1]] < nums[i]:
    #             q.pop()
    #         q.append(i)
    #         if i >= k-1:
    #             maxs.append(nums[q[0]])
    #     return maxs


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(Solution().maxSlidingWindow([1], 1))
