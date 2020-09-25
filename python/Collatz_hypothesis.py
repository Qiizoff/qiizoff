# import random
n = 0
y = 0
num = 0
big = 0
big1 = 0
big2 = 0
while n < 1000000:
    n += 1
    # y = random.randint(0, 100)
    y += 1
    # print('\nЧисло:', y)
    big1 = y
    y1 = y
    while y1 > 1:
        if y1 % 2 == 0:
            num += 1
            y1 = y1//2
            # print('ЧЕТ:', y)
        else:
            y1 = (y1*3)+1
            num += 1
            # print('НЕЧ:', y1)

    # print('Num:', num)
    if big < num:
        big = num
        big2 = big1
        num = 0
    else:
        num = 0
print('BIG:', big, 'NUM:', big2)
