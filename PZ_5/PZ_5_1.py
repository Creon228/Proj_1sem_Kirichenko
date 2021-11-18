#Практическая работа №5
# Вариант 8

def risunok(schet): #функция, прибавляющая по одной звездочке каждую итерацию цикла
    i = 0
    schet = int(schet)
    while i <= schet:
        print("*" * i)
        i += 1


a = input("Введите количество звездочек: ")
risunok(a)