# Exception

Python raises an exception whenever an error occurs.

Exceptions can be handled by the program, preventing the interpreter from halting.

Unhandled exceptions will cause Python to halt execution and prints a stack tree.

Exceptions are objects! They have classes with constructors.

Exceptions enable non-local continuations of control:

If f calls g and g calls h, exceptions can shift control from h to f without waiting for g to return.

# Raising Error
## Assert statements 

```python
assert <expression>, <string>
```

Assertions are designed to be used liberally. They can be ignored to increase efficiency by running Python with the "-O" flag. "O" stands for optimized.

```python
python3 -O
```

Whether assertions are enabled is governed by a bool __debug__.

```
➜  cs61a git:(master) ✗ python3 -O
Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct  6 2017, 12:04:38)
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> __debug__
False
>>> assert False, "Error"
```

## Raise Statements

```python
raise <expression>
```

<expression> must evaluate to a subclass of BaseException or an instance of one.
Exceptions are constructed like any other object. E.g., TypeError('Bad argument!')

- TypeError: A function was passed the wrong number/type of argument
- NameError: A name wasn't found
- KeyError: A Key wasn't found in dictionary
- RuntimeError: Catch-all for troubles during interpretation

# Handle exceptions
## Try statements

```python
try:
    <try suite>
except <exception class> as <name>:
    <except suite>
```
