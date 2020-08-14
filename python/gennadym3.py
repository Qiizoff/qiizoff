import random
mylist = list()
n = 0
while n <= 9:
    n += 1
    b = 100
    i = 0
    while i <= 9:
        i += 1
        y = random.randint(0, 1)
        if y == 1:
            b = b+50
            print('+', '%.5f' % b)
        else:
            b = b-50
            print('-', '%.5f' % b)
    print('\nБаланс:', n, '=', '%.1f' % b)
