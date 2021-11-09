import math
razmer = input("Введите размер файла в байтах") #Ввод исходных данных.
while type (razmer) != int : #Проверка на исключения.
    try:
        razmer = int(razmer)
    except ValueError :
        print("Введены некорректные данные")
        razmer = input("Введите размер файла в байтах")
print('Размер файла в килобайтах ', razmer//1024) #Вывод конечных данных.