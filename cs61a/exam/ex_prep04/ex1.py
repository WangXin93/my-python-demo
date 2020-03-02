a = [1, 2, 3, 4, 5]
a.pop(3)
b = a[:]
a[1] = b
b[0] = a[:]
b.pop()
b.remove(2)
c = [].append(b[1])
a.insert(b.pop(1), a[-3:4:3])
b.extend(b)
if b == b[:] and b[1][1][0] is b[0][1][1]:
        a, b, c = [c] + a[-4:4:2]
