#Практическая работа №4
#Вариант №8

import math
def proverka(znach):
    while type(znach) !=int:
        try:
            znach = int(znach)
        except ValueError:
            print("Вы ввели некорректное значение")
            znach = input("Введи правильное значение")
    else:
        return znach
a = input("Введите первое значение")
a = proverka(a)
b = input("Введите второе значение")
b = proverka(b)
summa = a**2
while a<=b:
    summa = summa + a**2
    a+=1
print(summa)

