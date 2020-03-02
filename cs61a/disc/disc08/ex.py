class nil:
    """Represents the special empty pari nil in Scheme."""
    def __repr__(self):
        return 'nil'
    def __len__(self):
        return 0
    def __getitem__(self, i):
        raise IndexError('Index out of range')
    def map(self, fn):
        return nil

nil = nil()

class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.second)
    def __len__(self):
        return 1 + len(self.second)
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.second[i-1]
    def map(self, fn):
        return Pair(fn(self.first), self.second.map(fn))

"""
# Q1.1
> (+ 1 2 (- 3 4))
Pair('+', Pair(1, Pair(2, Pair(Pair('-', Pair(3, Pair(4, nil)))), nil))))

> (+ 1 (* 2 3) 4)
Pair('+', Pair(Pair('*', 2, 3, nil), Pair(4, nil)))

# Q1.2
>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
(+ 1 2 3 4)

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))
"""
from operator import add, sub, mul, truediv, lt, gt, eq

OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    '<': lt,
    '>': gt,
    '=': eq
}

def calc_eval(exp):
    """Evaluates a Calculator expression represented as a Pair."""
    if isinstance(exp, Pair):
        if exp.first in OPERATORS:
            return calc_apply(calc_eval(exp.first),
                              list(exp.second.map(calc_eval)))
        elif exp.first == 'and':
            return calc_and_eval(exp.second)
    elif exp in OPERATORS:
        return OPERATORS[exp]
    else: # Atomic expressions
        return exp

def calc_apply(op, args):
    """Applies an operator to a Pair of arguments."""
    return op(*args)

def calc_and_eval(operands):
    """Eval the *and* subexpressions."""
    if operands is nil:
        return True
    while operands.second is not nil:
        if calc_eval(operands.first) == False:
            return False
        operands = operands.second
    return calc_eval(operands.first)

