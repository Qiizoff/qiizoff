from numpy import base_repr

s = 'td78nv'

for i in range(int(s, 36), 0, -1):
    print(i)
    print(base_repr(i, 36).lower())
    if i == 1775102971:
        break
