"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и 
Вы должны реализовать функционал для изменения и удаления данных"""


import csv

def AddContact():                # блок ввода               
    with open('phone_book.csv', "a") as file:
        column_names=['lastname', 'name', 'phone_number']
        lastname = input("Введите фамилию  ")
        name = input("Введите имя  ")
        phone_number = input("Введите номер телефона  ")
        writer = csv.DictWriter(file, column_names)
        writer.writerow({"lastname": lastname, "name": name, "phone_number": phone_number})



def FullList():              # блок чтения/вывода всех контактов             
    with open('phone_book.csv', "r") as file:
        data = csv.DictReader(file)
        sortedList = sorted(data, key = lambda contact: contact["lastname"])   #сортировка
        for person in sortedList:
            print(f"{person['lastname']}, {person ['name']}, {person['phone_number']}")

def find_info():        # блок поиска
    data = open('phone_book.csv', 'r')
    find = input("Введите имя, фамилию или номер  ")
    count = 0
    for line in data:
        if find in line:
            print(line)
            count += 1
    if count == 0:
        print("Запись не найдена")
    data.close()

def change_info():           # блок изменения записи
    with open('phone_book.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            old_word = input("Что требуется изменить?  ")
            new_word = input(f"На что хотите заменить {old_word}?   ")
            for line in rows:
                if old_word in line:
                    index = line.index(old_word)
                    line[index] = new_word
    with open('phone_book.csv', 'w', newline='') as file:
        csv.writer = csv.writer(file)
        for line in rows:
            csv.writer.writerow(line)
    print("Запись изменена")    


def delete_from_pb():          # блок удаления записи
    with open('phone_book.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    word = input("Что хотите удалить? ")
    for line in rows:
        if word in line:
            rows.remove(line)
    with open('phone_book.csv', 'w') as file:   
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Запись удалена")


# a = AddContact()
# b = FullList()
# c = change_info()
# d = delete_from_pb()
# f = find_info()