from typing import List

class Solution:
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     num = int(''.join(str(x) for x in digits)) + 1
    #     out = [int(x) for x in str(num)]
    #     return out 

    def plusOne(self, digits: List[int]) -> List[int]:
        addOneBefore = False
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if addOneBefore:
                digits[i] += 1
                addOneBefore = False
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                else:
                    addOneBefore = True
        return digits

if __name__ == "__main__":
    print(Solution().plusOne([1,2,3]))
    print(Solution().plusOne([4, 3, 2, 1]))
    print(Solution().plusOne([9]))

