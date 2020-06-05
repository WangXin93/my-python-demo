class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 = n1*10 + ord(num1[i]) - ord('0')
        for i in range(len(num2)):
            n2 = n2*10 + ord(num2[i]) - ord('0')
        mul = n1 * n2
        s = []
        while True:
            s.append(str(mul % 10))
            mul = mul // 10
            if mul == 0:
                break
        return ''.join(s[::-1])

if __name__ == "__main__":
    print(Solution().multiply("123", "456"))
    print(Solution().multiply("1", "1"))
    print(Solution().multiply("0", "0"))
