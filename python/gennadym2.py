import random
mylist = list()
n = 0
while n <= 99:
    n += 1
    # print('\nЦикл:', n)
    b = 100
    i = 0
    while i <= 99:
        i += 1
        y = random.randint(0, 1)
        if y == 1:
            b = b+50
        else:
            b = b-50
    mylist.append(b)
mylist2 = (sorted(mylist))
for x in mylist2:
    print('Паралельные реальности:', '=', '%.1f' % x)
