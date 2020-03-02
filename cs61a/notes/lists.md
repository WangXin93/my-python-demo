# Lists operations

Assume that before each example below we execute:
```
s = [2, 3]
s = [5, 6]
```

- append
```
s.append(t)
t = 0
```

- extend
```
s.extend(t)
t[1] = 0
```

- addtion & slicing
```
a = s + [t]
b = a[1:]
a[1] = 9
b[1][1] = 0
```

- The list function
also creates a new list containing existing elements
```
t = list(s)
s[1] = 0
```

- slice assignment
replaces a slice with new values
```
s[0:0] = t
s[3:] = t
t[1] = 0
```
