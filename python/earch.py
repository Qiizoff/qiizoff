import math

R = 6372000
h = float(input('Высота над уровнем моря:'))
d = ((((R+h)**2)-(R**2))**0.5)
d = round(d/1000, 2)
d1 = math.acos(1/(1+h/R))*R
d1 = round(d1/1000, 2)
print(d, 'км')
print(d1, 'км')


# http://www.randewy.ru/nav/ucheb6.html
# https://yandex.ru/q/question/kakoi_uchastok_prostranstva_my_vidim_do_1d0df81e/
