import random
n = 9
num = 0
while n < 10:
    n += 1
    y = random.randint(0, 100)
    y = 2357899
    print('\nЧисло:', y)
    while y > 1:
        if y % 2 == 0:
            num += 1
            y = y//2
            print('ЧЕТ:', y)
        else:
            y = (y*3)+1
            num += 1
            print('НЕЧ:', y)
    print('Num', num)
    num = 0


# def even_or_odd(a):

#     if a % 2 == 0:
#         print('Четное число')
#     else:
#         print('Нечентное число')
