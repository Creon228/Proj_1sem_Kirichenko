# Практическая работа №6
# Вариант 8
# Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке четные числа в порядке убывания их индексов, а также их количество K.


spisok = [input('Введите число') for i in range(10)]
even_spisok = []
for i in range(len(spisok)):
    if spisok[i] % 2 == 0:
        even_spisok.append([spisok[i]])
print(f'Элементы: {reversed(even_spisok)}, их количество: {len(even_spisok)}')