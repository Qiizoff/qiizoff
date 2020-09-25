def even_or_odd(a):

    if a % 2 == 0:
        print('Четное число')
    else:
        print('Нечентное число')


even_or_odd(3)


stats = [["сила", 0], ["здоровье", 1], ["мудрость", 0], ["ловкость", 0]]


def add_one(skill):
    for i in stats:
        if i[0] == skill:
            i[1] += 1


add_one('сила')
print(stats)
