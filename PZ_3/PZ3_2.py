import math


def proverka(c):  # функция проверки
    while type(c) != float:
        try:
            c = float(c)
            if (c < 0):
                print("Вы ввели некорректное значение")
                c = input("Введите корректное значение ")
        except ValueError:
            print("Вы ввели некорректное значение")
            c = input("Введите корректное значение ")
    else:
        return c


def proverka_2(v):  # функция проверки
    while type(v) != int:
        try:
            v = int(v)
            if (5 > v < 0):
                print("Вы ввели некорректное значение")
                v = input("Введите корректное значение ")
        except ValueError:
            print("Вы ввели некорректное значение")
            v = input("Введите корректное значение ")
    else:
        return v


def perevod(var, znach):  # функция перевода числа
    if (var == 1):
        print(znach / 10, " метров")
    elif (var == 2):
        print(znach * 1000, " метров")
    elif (var == 3):
        print(znach, " метров")
    elif (var == 4):
        print(znach / 1000, " метров")
    elif (var == 5):
        print(znach / 100, " метров")
    return "----------------------------------------------------"


variant = input("Выберите единицу измерения : 1-дециметр 2-километр 3-метр 4-миллиметр 5-сантиметр ")  # ввод варианта
variant = proverka_2(variant)
dlina = input("Введите длину ")  # ввод исходного значения
dlina = proverka(dlina)
otvet = perevod(variant, dlina)
print(otvet)  # вывод конечных данных
