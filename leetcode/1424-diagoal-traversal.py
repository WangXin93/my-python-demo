from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = []
        for r, row in enumerate(nums):
            for c, num in enumerate(row):
                sumIdx = r + c
                if len(groups) <= sumIdx:
                    groups.append(list())
                groups[sumIdx].insert(0, num)
        rtn = []
        for group in groups:
            for num in group:
                rtn.append(num)
        return rtn

if __name__ == "__main__":
    print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(Solution().findDiagonalOrder([[1, 2, 3, 4, 5, 6]]))
    print(Solution().findDiagonalOrder([[14,12,19,16,9],[13,14,15,8,11],[11,13,1]]))