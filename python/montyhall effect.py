import random
print("\n0 - WIN \n1 - LOSE \n2 - LOSE\n")

door_list = [0, 1, 2]
i = 0
w = 0
l = 0

while i <= 99:
    print("------ №:", i, "------")
    random.shuffle(door_list)
    print("Список дверей:", door_list)
    n = random.choice(door_list)
    print("Выбор игрока:", n)
    o = random.choice(door_list)
    t = 0
    while t != 1:
        if o == n or o == 0:
            o = random.choice(door_list)
            # print("Попытки ведущего:", o)
        else:
            print("Выбор ведущего:", o)
            t += 1
# Меняем решение на основании выбора ведущего
    if n == 0 and o == 1:
        n = 2
        print("Игрок выбрал дверь:", n)
    elif n == 0 and o == 2:
        n = 1
        print("Игрок выбрал дверь:", n)
    elif n == 1 and o == 2 or n == 2 and o == 1:
        n = 0
        print("Игрок выбрал дверь:", n)
    else:
        print("Ошибка:", n)
# Подсчет результаов
    if n == 0:
        w += 1
    else:
        n > 0
        l += 1
    i += 1

print("WIN", w)
print("LOSE", l)
