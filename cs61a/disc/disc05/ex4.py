class A:
    def f(self):
        return 2
    def g(self, obj, x):
        if x == 0:
            return A.f(obj)
        return obj.f() + self.g(self, x - 1)

class B(A):
    def f(self):
        return 4

x, y = A(), B()

print(x.f()) # 2

# B.f() # Error

print(x.g(x, 1)) # 4

print(y.g(x, 2))