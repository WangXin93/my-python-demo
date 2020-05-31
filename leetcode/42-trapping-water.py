from typing import List


class Solution:
    def two_pointer(self, height):
        if len(height) < 2:
            return 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[0], height[-1]
        pool = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    pool += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    pool += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return pool

    def stack(self, height):
        if len(height) <= 2:
            return 0
        stack = []
        pool = 0
        for i in range(len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop(-1)
                if len(stack) == 0:
                    break
                dist = (i - stack[-1] - 1)
                h = min(height[i], height[stack[-1]]) - height[top]
                pool += h * dist
            stack.append(i)
        return pool

    def dp(self, height):
        l2r = []
        for h in height:
            if len(l2r) == 0:
                l2r.append(h)
            elif h > l2r[-1]:
                l2r.append(h)
            else:
                l2r.append(l2r[-1])
        r2l = []
        for h in height[::-1]:
            if len(r2l) == 0:
                r2l.append(h)
            elif h > r2l[-1]:
                r2l.append(h)
            else:
                r2l.append(r2l[-1])
        r2l.reverse()
        pool = 0
        for i, h in enumerate(height):
            pool += min(l2r[i], r2l[i]) - h
        return pool

    def brute_force(self, height):
        pool = 0
        for mid in range(len(height)):
            left, right = mid, mid
            # Find left max
            for i in range(left, -1, -1):
                if height[i] > height[left]:
                    left = i
            # Find right max
            for i in range(right, len(height)):
                if height[i] > height[right]:
                    right = i
            pool += min(height[left], height[right]) - height[mid]
        return pool

    def trap(self, height: List[int]) -> int:
        return self.stack(height)
        return self.two_pointer(height)
        return self.dp(height)
        return self.brute_force(height)


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(Solution().trap([4, 2, 3]))
