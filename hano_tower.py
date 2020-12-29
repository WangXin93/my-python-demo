"""
https://www.bilibili.com/video/BV1CV411z798?p=6
"""

def hano_2disk(src, aux, tgt):
    aux.append(src.pop(-1))
    tgt.append(src.pop(-1))
    tgt.append(aux.pop(-1))

def hano_3disk(src, aux, tgt):
    tgt.append(src.pop(-1))
    aux.append(src.pop(-1))
    aux.append(tgt.pop(-1))
    tgt.append(src.pop(-1))
    src.append(aux.pop(-1))
    tgt.append(aux.pop(-1))
    tgt.append(src.pop(-1))

def hano_ndisk(src, aux, tgt, n):
    if n == 1:
        tgt.append(src.pop(-1))
    else:
        hano_ndisk(src, tgt, aux, n-1)
        tgt.append(src.pop())
        hano_ndisk(aux, src, tgt, n-1)

src = [3, 2, 1]
aux = []
tgt = []
hano_3disk(src, aux, tgt)
print(f"{src}, {aux}, {tgt}")

src = [4, 3, 2, 1]
aux = []
tgt = []
hano_ndisk(src, aux, tgt, 4)
print(f"{src}, {aux}, {tgt}")
