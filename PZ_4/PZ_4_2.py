import math

procent = input("Введите процент вклада")
while type(procent) != int
    try:
        procent = int(procent)
        if (0 < procent < 25):
            print("Вы ввели некорректное значение")
            procent = input("Введите процент вклада")
    except ValueError:
        print("Вы ввел некорректное значение")
