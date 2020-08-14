import random
b = 100
n = 0

while n <= 30:
    n += 1
    # print('Цикл:', n)
    i = 0
    while i <= 100:
        i += 1
        y = random.randint(0, 1)
        # print('Рандом:', y)
        if y == 1:
            b = b+50
        else:
            b = b-40
    print('Паралельная реальность №:', n, '=', b)
