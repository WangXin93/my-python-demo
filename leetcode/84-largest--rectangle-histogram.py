from typing import List
from itertools import combinations_with_replacement


class Solution:
    def brute_force(self, heights: List[int]) -> int:
        maxArea = 0
        for start, end in combinations_with_replacement(range(len(heights)), 2):
            w = end - start + 1
            h = min(heights[start:end+1])
            area = w * h
            maxArea = max(area, maxArea)
        return maxArea

    def divide_and_conquer(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        minH, minIdx = float('inf'), 0
        maxArea = 0
        for idx, h in enumerate(heights):
            if h < minH:
                minH = h
                minIdx = idx
        maxArea = max(minH * len(heights), maxArea)
        left = self.divide_and_conquer(heights[:minIdx])
        right = self.divide_and_conquer(heights[minIdx+1:])
        maxArea = max(maxArea, left, right)
        return maxArea

    def clever(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.clever(heights)


if __name__ == "__main__":
    # heights = [2,1,5,6,2,3]
    heights = [2,1,3,3,2,3]
    print(Solution().largestRectangleArea(heights))
    # heights = []
    # print(Solution().largestRectangleArea(heights))
    # heights = [1]
    # print(Solution().largestRectangleArea(heights))
