from random import choice
import time

correctPassword = "1234"
wrongPasswords = set()

length = len(correctPassword)
chars = "123456789"
run = True
d = 0
t1 = time.time()
while run:
    password = ''
    d += 1
    for i in range(length):
        password += choice(chars)

    if password == correctPassword:
        run = False
        print("d:", d)
        print(password + " is correct")
        print('time: ', time.time() - t1)
    else:
        wrongPasswords.add(password)
