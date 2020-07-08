from numpy import base_repr

s = 'td78nv'

for i in range(int(s, 36), 0, -1):
    print(i)
    p = (base_repr(i, 36).lower())
    print(p)
    if i == 1775687971:
        break
