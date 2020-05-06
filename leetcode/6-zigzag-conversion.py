from math import ceil

class Solution:
    def convert3(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range (numRows)]
        for r in range(numRows):
            print(out)
            if r == 0:
                k=0
                while k*(2*numRows - 2) < len(s):
                    out += s[k*(2*numRows - 2)]
                    k += 1
            elif r == numRows-1:
                k=0
                while (k+1)*(2*numRows - 2) - r < len(s):
                    out += s[(k+1)*(2*numRows - 2) - r] 
                    k += 1
            else:
                k = 0
                while True:
                    left = k*(2*numRows - 2) + r
                    right = (k+1)*(2*numRows - 2) - r
                    if left < len(s):
                        out += s[left]
                    if right < len(s):
                        out += s[right]
                    if left >= len(s):
                        break
                    else:
                        k += 1
        return out

    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range (numRows)]
        r, c = 0, 0
        dr, dc = 1, 0
        for char in s:
            rows[r].append(char)
            if r==0:
                dr, dc = 1, 0
            elif r==(numRows-1):
                dr, dc = -1, 1
            r += dr
            c += dc
        out = ""
        for row in rows:
            for char in row:
                out += char
        return out

    def convert(self, s: str, numRows: int) -> str:
        lin = 0
        direction = 1
        out = [""] * numRows
        for char in s:
            out[lin] += char
            if numRows > 1:
                lin += direction
                if lin == 0 or lin == numRows - 1:
                    direction *= -1
        return "".join(out)

class Solution(object):
    def convert(self, s, numRows):
        if s == None:
            return s
        if numRows == 0:
            return s
        if numRows == 1:
            return s
        rstr = ""
        for i in range(numRows):
            if i == 0:
                rstr += s[::numRows + (numRows-2)]
            elif i == numRows-1:
                rstr += s[i::numRows + (numRows-2)]
            else:
                spacea = 2*numRows - 2 - 2*i
                spaceb = 2*i
                counter = 0
                j = i
                while j < len(s):
                    rstr += s[j]
                    if counter % 2 == 0:
                        j+= spacea
                    else:
                        j+=spaceb
                    counter +=1
        return rstr

if __name__ == "__main__":
    print(Solution().convert("PAYPALISHIRING", 3))
    print(Solution().convert("PAYPALISHIRING", 4))
    print(Solution().convert("PAYPALISHIRING", 5))
