def sum_digit(n):
    if n // 10 == 0:
        return n
    else:
        return n % 10 + sum_digit(n // 10)

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n//10)
shrink = lambda n: f_then_g(print, shrink, n//10)

# Fibonacci
import functools
@functools.lru_cache(3)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Counting Partitions
def count_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0 
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)