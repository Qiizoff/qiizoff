from numpy import base_repr

s = 'tcum81'
for i in range(int(s, 36), 0, -1):
    # print(i)
    print(base_repr(i, 36).lower())
    break
