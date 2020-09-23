import random
n = 0
num = 0
while n < 10:
    n += 1
    y = random.randint(0, 10654900)
    print('Число:', y)
    while y > 1:
        if y % 2 == 0:
            num += 1
            y = y//2
            # print('ЧЕТ:', y)
        else:
            y = (y*3)+1
            num += 1
            # print('НЕЧ:', y)
    print('Num', num)

# def even_or_odd(a):

#     if a % 2 == 0:
#         print('Четное число')
#     else:
#         print('Нечентное число')
