#Практическая работа №4
#Вариант 8

import math
p = input("Введите процент вклада") #ввод исходных данных
while type(p) != float: #проверка исключений
    try:
        p = float(p)
        if (0>p>25):
            print("Вы ввели некрроктное значение")
            p = input("Введите процент вклада")
    except ValueError:
        print("Вы ввели некрроктное значение")
        p = input("Введите процент вклада")

vklad = 1000
mes = 1
itog = 0

while itog < 1100 : #цикл, сичтающий месяцы
    mes += 1
    itog = itog +(vklad + (vklad/100*p))
print("Через ", mes, " месяцев вклад будет составлять ", itog)
