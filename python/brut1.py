import time

password = '008'

# VALID_CHARS = 'abcdefghijklmnopqrstuvwxyz0123456789'

pass_int = int(password)
t1 = time.time()

for i in range(0, 1000):

    print('pass:', i)
    if i == pass_int:
        # print('password is', i)
        print('password is "{:0{w}}"'.format(i, w=len(password)))
        break

print('time: ', time.time() - t1)
