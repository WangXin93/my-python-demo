from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        areaMax = (j-i) * min(height[i], height[j])
        while (i < j):
            print("i: {}, j: {}, areaMax: {}".format(i, j, areaMax))
            if height[i] < height[j]:
                i = i+1
            else:
                j = j - 1
            areaNew = (j-i) * min(height[i], height[j])
            print(areaNew)
            areaMax = max(areaNew, areaMax)
        return areaMax

if __name__ == "__main__":
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
