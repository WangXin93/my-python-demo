# Scheme Fundamentals

Scheme programs consist of expressions, which can be:

- Primitive expressions: 2, 3.3, true, +, quotient, ...

- Combinations: (quotient 10 2), (not true), ...

Numbers are self-evaluating; symbols are bound to values.
Call expressions include an operator and 0 or more operands in parantheses.


```lisp
> (quotient 10 2)
5
> (quotient (+ 8 7) 5)
3
> (+ (* 3
        (+ (* 2 4)
           (+ 3 5)))
     (+ (- 10 7)
        6))
57
```

# Special Forms

A combination that is not a call expression is a special form:

- If expression: (if <predicate> <consequent> <alternative>)
- And an or: (and <e1> ... <e2>), (or <e1> ... <e2>)
- Binding symbold: (define <symbol> <expression>)

```
> (define pi 3.14)
> (* pi 2)
6.28
```
- New procedures: (define (<symbol> <formal parameters>) <body>)

```
> (define (abs x)
    (if (< x 0)
        (- x)
        x))
> (abs -3)
3
```

```
scm> (define (square x) (* x x))
square
scm> (square 16)
256
scm> (define (average x y)
     (/ (+ x y) 2))
average
scm> (average 2 8)
5
scm> (define (sqrt x)
        (define (update guess)
           (if (= (square guess) x)
                guess
                (update (average guess (/ x guess)))))
        (update 1))
sqrt
scm> (sqrt 4)
2
```

```python
def sqrt(x):
    def update(guess):
        print(guess)
        if guess * guess == x:
            return guess
        else:
            return update((guess + x/guess)/2)
    return update(1)
sqrt(4)
```

# Lambda Expressions

Lambda expressions evaluate to anonymous procedures.

```
(lambda (<formal-parameters>) <body>)
```

Two equivalent expressions:
```
(define (plus4 x) (+ x 4))
(define plus4 (lambda (x) (+ x 4)))
```
```
((lambda (x y z) (+ x y (squre z))) 1 2 3)
```

# Pairs and Lists
In the late 1950s, computer scientists used confusing names
- cons: Two- argument procedure that creates a pair
- car: Procedure that returns the first element of a pair
- cdr: Prodedure that returns the second element of a pair
- nil: The empty list
- A (non-empty) list in Scheme is a pair in which the second element is nil or a Scheme list
- Important! Scheme lists are written in paratheses seperated by spaces
- A dotted list has some value for the second element of the last pair that is not a list
```
scm> (cons 1 (cons 2 nil))
(1 2)
scm> (define x (cons 1 2))
x
scm> x
(1 . 2)
```

```
(define (length s)
  (if (null? s)
     0
     (+ 1 (length (cdr s)))))
```

# Symbolic Programming

Symbols normally refer to values; how do we refer to symbols?

```
> (define a 1)
> (define b 2)
> (list a b)
(1 2)
```

Quotation is used to refer to symbols directly in Lisp.

```
> (list 'a 'b)
(a b)
> (list 'a b)
(a 2)
```

Quotation can also be applied to combinations to form lists.

```
> (car '(a b c))
a
> (cdr '(a b c))
(b c)
```
