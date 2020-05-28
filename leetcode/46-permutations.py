from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def gen(nums):
            if len(nums) == 1:
                yield nums
            for i, num in enumerate(nums):
                for tail in gen(nums[:i] + nums[i+1:]):
                    yield [num] + tail
        return list(gen(nums))


if __name__ == "__main__":
    print(Solution().permute([1, 2, 3]))
