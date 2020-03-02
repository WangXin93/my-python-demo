# Control

## 1.5.1 Statements
assignment, def, and return are statements
Rather than being evaluated, statements are executed
At its highest level, the Python interpreter's job is to execute programs, composed of statements
Statements govern the relationship among different expressions in a program and what happens to their results.

## 1.5.2 Compound Statements
Python code is a sequence of statements
Compound statements typically span multiple lines and start with a one-line header ending in a colon, which identifies the type of statement. Together, a header and an indented suite of statements is called a clause
```
<header>:
    <statement>
    <statement>
    ...
<separating header>:
    <statement>
    <statement>
    ...
...
```
## 1.5.3 Defining Functions II: Local Assignment

## 1.5.4 Conditional Statements
A conditional statement in Python consists of a series of headers and suites: a required if clause, an optional sequence of elif clauses, and finally an optional else clause:
```
if <expression>:
    <suite>
elif <expression>:
    <suite>
else:
    <suite>
```
every built-in kind of data in Python has both true and false value.
Logical expressions have corresponding evaluation procedures. These procedures exploit the fact that the truth value of a logical expression can sometimes be determined without evaluating all of its subexpressions, a feature called short-circuiting.

## 1.5.5 Iteration
Only through repeated execution of statements do we unlock the full potential of computers
A while clause contains a header expression followed by a suite:
```
while <expression>:
    <suite>
To execute a while clause:
```
Evaluate the header's expression.
If it is a true value, execute the suite, then return to step 1.
## 1.5.6 Testing
Testing a function is the act of verifying that the function's behavior matches expectations
the globals function returns a representation of the global environment
```
>>> from doctest import testmod
>>> testmod()
TestResults(failed=0, attempted=2)
```

```
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```
```
$ python3 -m doctest <python_source_file>
```
