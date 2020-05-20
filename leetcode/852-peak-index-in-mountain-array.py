from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left

    # def peakIndexInMountainArray(self, A: List[int]) -> int:
    #     left, right = 0, len(A)-1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if A[mid-1] < A[mid] > A[mid+1]:
    #             return mid
    #         elif A[mid-1] < A[mid] < A[mid+1]:
    #             left = mid + 1
    #         elif A[mid-1] > A[mid] > A[mid+1]:
    #             right = mid - 1

    # Approach3 Golden Section Search

if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([0, 1, 0])) # 3