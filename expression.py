"""
How do we evaluate ((2*17)+(2*(3+(4*9))))?

if expression is a number, return expression
Otherwise, break up expression by its operator:
    leftResult = evaluate(leftExpression)
    rightResult = evaluate(rightExpression)
    return leftResult operator rightResult
"""
from string import digits
from operator import add, mul, sub, truediv

OPERATORS = {
        '+': add,
        '*': mul,
        '-': sub,
        '/': truediv
}

def find_op_idx(exp):
    parent = 0
    idx = -1
    for i, c in enumerate(exp):
        if c == '(':
            parent += 1
        elif c == ')':
            parent -= 1
        if c in OPERATORS and parent == 1:
            idx = i
    return idx

def expression(exp):
    if all(c in digits for c in exp):
        return float(exp)
    else:
        op_idx= find_op_idx(exp)
        op = exp[op_idx]
        left = exp[1:op_idx]
        right = exp[op_idx+1:-1]
        left = expression(left)
        right = expression(right)
        return OPERATORS[op](left, right)

print(expression("((2*17)+(2*(3+(4*9))))"))
