M4F = input("M spotting F: ")
F4M = input("F spotting M: ")
F4F = input("F spotting F: ")
M4M = input("M spotting M: ")
assert M4F.isdigit()
assert F4M.isdigit() 
assert F4F.isdigit()
assert M4M.isdigit()
M4F = int(M4F)
F4M = int(F4M)
F4F = int(F4F)
M4M = int(M4M)

axis = "M4F\tF4M\tF4F\tM4M"
for i in range(20):
    if 10 - i//2 <= M4F:
        m4f = '###'
    else:
        m4f = '   '

    if 10 - i//2 <= F4M:
        f4m = '###'
    else:
        f4m = '   '

    if 10 - i//2 <= F4F:
        f4f = '###'
    else:
        f4f = '   '

    if 10 - i//2 <= M4M:
        m4m = '###'
    else:
        m4m = '   '
    print('%s\t%s\t%s\t%s' % (m4f, f4m, f4f, m4m))
print(axis)
