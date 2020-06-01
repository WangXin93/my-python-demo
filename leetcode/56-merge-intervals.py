"""
You can image this problem like each interval is a depart and land time for a place, for such many planes, you compute which interval there is at least one plane in the sky.
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        out = []
        for interval in sorted_intervals:
            if len(out) == 0:
                out.append(interval)
            if interval[0] <= out[-1][1]:
                out[-1][1] = max(interval[1], out[-1][1])
            else:
                out.append(interval)
        return out


if __name__ == "__main__":
    print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution().merge([[1, 4], [4, 5]]))
    print(Solution().merge([[1, 4], [2, 3]]))
