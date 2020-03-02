# Higher-Order Functions

One of the things we should demand from a powerful programming language is the ability to build abstractions by assigning names to common patterns and then to work in terms of the names directly. 
Functions that manipulate functions are called higher-order functions

## 1.6.1 Functions as Arguments

## 1.6.2 Functions as General Methods
```
>>> def improve(update, close, guess=1):
        while not close(guess):
            guess = update(guess)
        return guess

>>> def golden_update(guess):
        return 1/guess + 1
>>> def square_close_to_successor(guess):
        return approx_eq(guess * guess, guess + 1)
>>> def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance
>>> improve(golden_update, square_close_to_successor)
1.6180339887498951
```
This example illustrates two related big ideas in computer science. 
* First, naming and functions allow us to abstract away a vast amount of complexity. While each function definition has been trivial, the computational process set in motion by our evaluation procedure is quite intricate. 
* Second, it is only by virtue of the fact that we have an extremely general evaluation procedure for the Python language that small components can be composed into complex processe

## 1.6.3 Defining Functions III: Nested Definitions
computing the square root of a number, in programming languages, "square root" is often abbreviated as sqrt. Repeated application of the following update converges to the square root of a:
```
>>> def average(x, y):
        return (x + y)/2
>>> def sqrt_update(x, a):
        return average(x, a/x)
```

```
>>> def sqrt(a):
        def sqrt_update(x):
            return average(x, a/x)
        def sqrt_close(x):
            return approx_eq(x * x, a)
        return improve(sqrt_update, sqrt_close)
```
sqrt_update refers to the name a, which is a formal parameter of its enclosing function sqrt. This discipline of sharing names among nested definitions is called lexical scoping.

We require two extensions to our environment model to enable lexical scoping.

Each user-defined function has a parent environment: the environment in which it was defined.
When a user-defined function is called, its local frame extends its parent environment.
The parent of a function value is the first frame of the environment in which that function was defined
When a user-defined function is called, the frame created has the same parent as that function.
By calling functions that were defined within other functions, via nested def statements, we can create longer chains.
The environment for this call to sqrt_update consists of three frames: the local sqrt_update frame, the sqrt frame in which sqrt_update was defined (labeled f1), and the global frame.

The sqrt_update function carries with it some data: the value for a referenced in the environment in which it was defined. Because they "enclose" information in this way, locally defined functions are often called closures.


## Functions as Returned Values
An important feature of lexically scoped programming languages is that locally defined functions maintain their parent environment when they are returned.

## 1.6.5 Example: Newton's Method
Newton's method is a classic iterative approach to finding the arguments of a mathematical function that yield a return value of 0
```
>>> def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update
>>> def find_zero(f, df):
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero)
>>> def square_root_newton(a):
        def f(x):
            return x * x - a
        def df(x):
            return 2 * x
        return find_zero(f, df)
>>> def power(x, n):
        """Return x * x * x * ... * x for x repeated n times."""
        product, k = 1, 0
        while k < n:
            product, k = product * x, k + 1
        return product
>>> def nth_root_of_a(n, a):
        def f(x):
            return power(x, n) - a
        def df(x):
            return n * power(x, n-1)
        return find_zero(f, df)
>>> nth_root_of_a(2, 64)
8.0
>>> nth_root_of_a(3, 64)
4.0
>>> nth_root_of_a(6, 64)
2.0
```

## 1.6.6 Currying
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument. More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y). Here, g is a higher-order function that takes in a single argument x and returns another function that takes in a single argument y. This transformation is called currying.
```
def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start += 1
map_to_range(0, 10, curried_pow(2))
```
Currying allows us to do so without writing a specific function for each number whose powers we wish to compute.
```
>>> def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g
>>> def uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f
pow_curried = curry2(pow)
pow_curried(2)(5)
map_to_range(0, 10, pow_curried(2))
```
The curry2 function takes in a two-argument function f and returns a single-argument function g, The uncurry2 function reverses the currying transformation, so that uncurry2(curry2(f)) is equivalent to f.
```
>>> uncurry2(pow_curried)(2, 5)
32
```
## 1.6.7 Lambda Expression
A lambda expression evaluates to a function that has a single return expression as its body. Assignment and control statements are not allowed.
Despite their unusual etymology, lambda expressions and the corresponding formal language for function application, the lambda calculus, are fundamental computer science concepts shared far beyond the Python programming community. 

## 1.6.8 Abstractions and First-Class Functions
As programmers, we should be alert to opportunities to identify the underlying abstractions in our programs, build upon them, and generalize them to create more powerful abstractions.
Elements with the fewest restrictions are said to have first-class status. Some of the "rights and privileges" of first-class elements are:

* They may be bound to names.
* They may be passed as arguments to functions.
* They may be returned as the results of functions.
* They may be included in data structures.

## 1.6.9 Decorators
```
>>> def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped
>>> @trace
    def triple(x):
        return 3 * x
>>> triple(12)
->  <function triple at 0x102a39848> ( 12 )
36
```
As usual, the function triple is created. However, the name triple is not bound to this function. Instead, the name triple is bound to the returned function value of calling trace on the newly defined triple function. In code, this decorator is equivalent to:
```
>>> def triple(x):
        return 3 * x
>>> triple = trace(triple)
```
