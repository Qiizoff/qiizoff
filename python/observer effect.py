import random
i = 0
v = 0
igor = 0
sergey = 0
while i <= 100:
    print("------ №:", i, "------")
    x = random.randint(1, 100)
    y = random.randint(0, 1)
    print("x:", x, "y:", y)
    igor += x
    print("Result Igor", igor)
    if y == 1:
        x = x*2
    else:
        x = x/2
    sergey += x
    print("Result Serg", sergey)
    i += 1

v = 1-(igor/sergey)
print("====================")
print("SUM Igor", igor)
print("SUM Sergey", sergey)
print("{:.1%}".format(v))
