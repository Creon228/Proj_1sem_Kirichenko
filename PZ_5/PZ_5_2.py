# Практическая работа №5
# Вариант 8

def addleftdigit(d, k):
    global chislo
    d = str(d) #присвоение переменным строковый тип
    k = str(k)
    chislo = d + k #сложение строк
    return chislo


chislo = input("введите целое положительное число") #ввод исходных данных

while type(chislo) != int:
    try:
        chislo = int(chislo)
        if chislo < 1:
            print("Вы ввели некорректное значение")
            chislo = input("введите целое положительное число ")

    except ValueError:
        print("Вы ввели некорректное значение")
        chislo = input("введите целое положительное число ")

d1 = input("введите первую цифру ")
d1 = int(d1) # присвоение переменным целочисленный тип

while d1<1 or d1>9:
    print("Вы ввели некорректное значение")
    d1 = input("введите первую цифру ")
    d1 = int(d1)

d2 = input("введите вторую цифру ")
d2 = int(d2)

while d2<1 or d2>9:
    print("Вы ввели некорректное значение")
    d2 = input("введите вторую цифру ")
    d2 = int(d2)

print(addleftdigit(d1, chislo)) #вызов функции для сложения строк
print(addleftdigit(d2,chislo))