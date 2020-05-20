from operator import add, sub, mul, floordiv

class Solution:
    opDict = {
        "*": mul,
        "/": floordiv,
        "+": add,
        "-": sub
    }
    opOrder = {
        "*": 1,
        "/": 1,
        "+": 0,
        "-": 0,
        None: 0
    }
    # def calculate(self, s: str) -> int:
    #     buf = list(s)
    #     res = None
    #     sym = None
    #     while len(buf) > 0:
    #         if buf[0] == " ":
    #             buf.pop(0)
    #         elif buf[0] in "0123456789":
    #             if sym is None:
    #                 newNum = self.readNum(buf)
    #                 res = newNum
    #             elif self.opOrder[self.nextSym(buf)] > self.opOrder[sym]:
    #                 subStr = self.readSubStr(buf)
    #                 newNum = self.calculate(subStr)
    #                 res = self.opDict[sym](res, newNum)
    #             else:
    #                 newNum = self.readNum(buf)
    #                 res = self.opDict[sym](res, newNum)
    #         elif buf[0] in "*/-+":
    #             sym = self.readSym(buf)
    #     return res

    def calculate(self, s: str) -> int:
        stack = []
        buf = list(s)
        sign = "+"
        while buf:
            if buf[0] == " ":
                buf.pop(0)
            elif buf[0] in "0123456789":
                if sign == "+":
                    stack.append(self.readNum(buf))
                elif sign == "-":
                    stack.append(-self.readNum(buf))
                elif sign == "*":
                    last = stack.pop()
                    stack.append(last * self.readNum(buf))
                elif sign == "/":
                    last = stack.pop()
                    if last >= 0:
                        stack.append(last // self.readNum(buf))
                    else:
                        stack.append(-(-last // self.readNum(buf)))
            elif buf[0] in "+-*/":
                sign = self.readSym(buf)
        return sum(stack)
        

    def nextSym(self, buf):
        for c in buf:
            if c in "+-*/":
                return c

    def readSubStr(self, buf):
        out = ""
        while buf and buf[0] not in "+-":
            out += buf.pop(0)
        return out

    def readNum(self, buf):
        out = 0
        while buf and buf[0] in "0123456789":
            out = out*10 + int(buf.pop(0))
        return out

    def readSym(self, buf):
        sym = buf.pop(0)
        return sym
            

if __name__ == "__main__":
    print(Solution().calculate("3+2*2")) # 7
    print(Solution().calculate(" 3+5 / 2 ")) # 5
    print(Solution().calculate("14/3*2")) # 8