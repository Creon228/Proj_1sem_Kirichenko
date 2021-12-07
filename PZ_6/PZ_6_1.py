# asd

from random import randint

my_list = [randint(-100, 100) for i in range(10)]
print(my_list)
k = 0
for el in reversed(my_list):
    if el % 2 == 0:
        print(el)
        k += 1
print(k)
