n = 70
num = 0
big = 0
vi = 0
for i in range(1, n):
    # print('Число:', i)
    vi = i
    while i > 1:
        if i % 2 == 0:
            i = i//2
            num += 1
            # print('ЧЕТ:', i)
        else:
            i = (i*3)+1
            num += 1
            # print('НЕЧ:', i)
    # print('Кол-во операций:', num)

    if big < num:
        big = num
        vnum = vi
        num = 0
    else:
        num = 0
print('\nНаибольшее кол-во операций:', big, '\nС числом:', vnum, '\n')
