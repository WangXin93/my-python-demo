"""
[Interval scheduling maximization](https://www.wikiwand.com/en/Interval_scheduling#/Interval_Scheduling_Maximization)

Steps:
    1. Sort all intervals by their ends
    2. Select the interval with eariest ends
    3. remove the next interval if there is a intersect with current interval, or remove the next interval and update the end to removed interval
    4. repeat until the input list to empty
"""

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        count = 0
        end = float('-inf')
        for interval in intervals:
            if interval[0] < end:
                count += 1
            else:
                end = interval[1]
        return count

if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1
    print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # 2
    print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]])) # 0
    print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]])) # 2
