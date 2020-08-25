import random
mylist = list()
n = 0
while n <= 99:
    n += 1
    # print('\nЦикл:', n)
    b = 1000
    i = 0
    while i <= 99:
        i += 1
        y = random.randint(0, 1)
        if y == 1:
            b = b*1.05
        else:
            b = b*0.975
    mylist.append(b)
mylist2 = (sorted(mylist))
for x in mylist2:
    print('Паралельные реальности:', '=', '%.1f' % x)
