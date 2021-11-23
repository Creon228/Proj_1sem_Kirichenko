#Практическая работа №4
#Вариант №8
#Даны два целых числа A и B (A < B). Найти сумму квадратов всех целых чисел от A до B включительно.

import math
def proverka(znach): #проверка исключений
    while type(znach) !=int:
        try:
            znach = int(znach)
        except ValueError:
            print("Вы ввели некорректное значение")
            znach = input("Введи правильное значение")
    else:
        return znach
a = input("Введите первое значение") #ввод исходных значений
a = proverka(a)
b = input("Введите второе значение")
b = proverka(b)
summa = a**2
while a<b: #нахождение суммы квадратов
    a += 1
    summa = summa + a**2
print(summa)
