"""
Postfix example

The tradition notation of algebraic examples on the math course is like:

5 * 4 - 8 / 2 + 9

However, these notations do not explicitly tell the order of the operations, you need additional parentheses like: (5 * 4) - (8 / 2) + 9, that is annoying. It would be nice if there were a better way to do arithmtic so that we didn't have to worry about order of opeartions. 

We can use "postfix" notations

5 4 * 8 2 / - 9 +

There is a simple and clever method using a stack to perform arithmetic on a postfix expression:

1. Read the input and push numbers onto a stack until you reach an operator.
2. When you see an operator, apply the operator to the two numbers that are popped from the stack.
3. Push the resulting value back onto the stack.
4. When the input is complete, the value left on the stack is the result.

*Postfix notation is also called "Reverse Polish Notation" (RPN) because in the 1920s a Polish logician named Jan Łukasiewicz invented "prefix" notation, and postfix is the opposite of postfix, and therefore so-called "Reverse Polish Notation"
"""

from operator import add, sub, mul, truediv

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

notation = "5 4 * 8 2 / - 9 +"

def postfix(notation):
    inp = []
    stack = []
    for c in notation.split():
        inp.insert(0, c)
    while inp:
        curr = inp.pop(-1)
        if curr in OPERATORS:
            operand2 = float(stack.pop(-1))
            operand1 = float(stack.pop(-1))
            stack.append(OPERATORS[curr](operand1, operand2))
        else:
            stack.append(curr)
    if stack:
        return stack[0]
    else:
        return 0

print(postfix(notation))
