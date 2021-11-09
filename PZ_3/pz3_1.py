import math
def proverka(c):   #проверяющая функция
    while type(c) != int:
        try:
            c = int(c)
        except ValueError:
            print("Вы ввели некорректное значение")
            c = input("Введите значение заново")
    else:
        return c
a = input("Введите первое число")   #Ввод исходных данных
a = proverka(a)
b = input("Введите второе число")
b= proverka(b)
if (a//2==0 & b//2==0):   #сравнение значений
    print("Выссказывание верно")
else :
    print("Высказывание неверно")