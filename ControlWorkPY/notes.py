import json
from datetime import datetime
from colorama import Fore, Style


def start():
    print(Fore.BLUE + 'Добро пожаловать в приложение "Заметки"' + Style.RESET_ALL)
    run()

def run():
    user_command = input(Fore.BLUE +
                        'Введите номер команды:\n'
                        '   1 - создать заметку\n'   
                        '   2 - прочитать заметку/заметки\n'  
                        '   3 - редактировать заметку\n'   
                        '   4 - удалить заметку\n'   
                        '   5 - выход\n'   
                        + Style.RESET_ALL)
    if user_command == "1":
        addNote(count_id())
    elif user_command == "2":
        findNote(count_id())
    elif user_command == "3":
        editNote()
    elif user_command == "4":
        deleteNote()
    elif user_command == "5":
        print("До свидания")
        exit(0)
    else:
        print("Введена неправильная команда. Выберете команду из списка")
        run()

def addNote(id_count):
    data = json_reader()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.today().strftime('%Y-%m-%d  %H:%m')

    new_note = {
        "id": id_count,
        "title": title,
        "body": body,
        "datatime": date,
    }

    data["notes"].append(new_note)

    json_writer(data)

    print("Заметка добавлена\n")
    run()

def findNote(count_check):
    check_on_exist(count_check)
    user_command = input("Введите команду (1 - показать все заметки, 2 - показать заметку по id, "
                         "3 - показать заметки по определенной дате): ")
    data = json_reader()
    if user_command == "1":
        print_all_notes(data)
        run()
    elif user_command == "2":
        print_by_id(data)
        run()
    elif user_command == '3':
        print_by_date(data)
        run()
    else:
        print("Введена некорректная команда.")
        findNote(count_id())

def check_on_exist(id_count):  
    if id_count == 1:
        print("Список заметок пуст.")
        run()

def print_all_notes(json_data):
    print("\nВсе сохраненные заметки: \n")
    for note in json_data['notes']:
        print_json_obj(note)

def print_by_date(json_data):
    user_date = input("Введите интересующую вас дату в формате 'YYYY-MM-DD': ")
    flag = True
    for note in json_data['notes']:
        if note['datatime'] == user_date:
            if flag:  
                flag = False
                print("\nВот все заметки по искомой дате: \n")
            print_json_obj(note)
    if flag:
        print("\nЗаметок по выбранной дате не обнаружено или дата введена в некорректном формате. \n")
    run()

def print_by_id(json_data):
    try:
        id_for_check = int(input("Введите id заметки: "))
    except ValueError:
        print("Введено некорректное значение, введите правильный id.")
        print_by_id(json_data)
    for note in json_data['notes']:
        if note['id'] == id_for_check:
            print("\nИскомая заметка: \n")
            print_json_obj(note)
            run()
    print(f"Заметка с id '{id_for_check}' не найдена.")
    run()

def editNote():
    data = json_reader()
    try:
        id_for_check = int(input("Введите id заметки подлежащей к изменению: "))
    except ValueError:
        print("Введено некорректное значение, введите правильный id.")
        editNote()
    for obj in data['notes']:
        if obj['id'] == id_for_check:
            id_note_edit(obj)
            json_writer(data)
            print(f"Заметка с id '{id_for_check}' успешна изменена.")
            run()
    print(f"Заметка с id '{id_for_check}' на найдена.")
    run()

def id_note_edit(o):
    new_title = input("Введите новый заголовок: ")
    new_body = input("Введите новый текст заметки: ")
    new_date = datetime.today().strftime('%Y-%m-%d')
    o['title'] = new_title
    o['body'] = new_body
    o['datatime'] = new_date

def deleteNote():
    data = json_reader()
    try:
        id_for_check = int(input("Введите id заметки которую хотите удалить: "))
    except ValueError:
        print("Введено некорректное значение, введите правильный id.")
        deleteNote()
    for obj in data['notes']:
        if obj['id'] == id_for_check:
            data['notes'].remove(obj)
            json_writer(data)
            print(f"Заметка с id '{id_for_check}' успешна удалена.")
            run()
    print(f"Заметка с id '{id_for_check}' не найдена.")
    run()

def json_reader():
    with open('notes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def json_writer(new_data):
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(new_data, file, indent=2, ensure_ascii=False)

def count_id():
    data = json_reader()
    count = len(data['notes']) + 1
    flag = True
    if count == 1:  
        flag = False
    while flag:
        for obj in data['notes']:
            if obj['id'] == count:
                count += 1
                flag = True
                break  
            else:
                flag = False
    return count

def print_json_obj(o):
    print(f"Заметка id '{o['id']}'")
    print(f"Заголовок: {o['title']}")
    print(f"Текст заметки: {o['body']}")
    print(f"Дата последнего действия: {o['datatime']}")
    print()

start()