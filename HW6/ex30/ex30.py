"""Заполните массив элементами арифметической
прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для
получения n-го члена прогрессии: a
n
 = a1
 + (n-1) * d.
Каждое число вводится с новой строки.

Ввод: 7 2 5
Вывод: 7 9 11 13 15

"""


a = int(input())
b = int(input())
c = int(input())

array = [0]*c

for i in range (0, c):
    if i == 0:
        array[0] = a 
    else:
        array[i] = array[0]+(i)*b    

print(array)



 
