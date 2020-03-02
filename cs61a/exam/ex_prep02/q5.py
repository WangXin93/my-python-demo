def mouse(n):
    if n >= 10:
        squeak = n // 100
        n = frog(squeak) + n % 10
    return n

def frog(croak):
    if croak == 0:
        return 1
    else:
        return 10 * mouse(croak + 1)

print(mouse(357))
