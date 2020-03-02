lamb = lambda lamb: lambda: lamb + lamb
print(lamb(1000)() + (lambda b, c: b() * b() - c)(lamb(2), 1))
