import json

with open('phonebook.json', 'w') as json_file:
    json_file.close()


def menu():
    print("""    Вітаю у моїй телефонній книзі!
    
    Обери, що ти хочеш зробити:
    1. Додати новий контакт
    2. Знайти існуючий контакт за ім`ям
    3. Знайти існуючий контакт за прізвищем
    4. Знайти існуючий контакт за ім`ям та прізвищем
    5. Знайти існуючий контакт за номером телефону
    6. Знайти існуючий контакт за містом
    7. Видалити контакт за номером телефону
    8. Обновити контакт за номером телефону
    9. Вийти з телефонної книги""")
    selection = input('Обери необхідне та введи відповідний номер: ')
    if selection == '1':
        add_new_entries()
    elif selection == '2':
        search_first_name()
    elif selection == '3':
        search_second_name()
    elif selection == '4':
        search_full_name()
    elif selection == '5':
        search_phone_number()
    elif selection == '6':
        search_city()
    elif selection == '7':
        del_record_by_phone()
    elif selection == '8':
        upd_record_by_phone()
    elif selection == '9':
        exit_program()


def add_new_entries():
    new_entries_dict = dict()
    new_entries_dict['phone'] = input('Введіть номер телефону: ')
    new_entries_dict['first_name'] = input('Введіть ім`я: ')
    new_entries_dict['second_name'] = input('Введіть прізвище: ')
    new_entries_dict['full_name'] = new_entries_dict['first_name'] + ' ' + new_entries_dict['second_name']
    new_entries_dict['city'] = input('Введіть місто проживання: ')
    with open('phonebook.json', 'a') as new_entries_file:
        full_info = json.dumps(new_entries_dict)
        new_entries_file.write(full_info)
        new_entries_file.close()


menu()
with open('phonebook.json') as rf:
    contacts = rf.read()
    print(contacts)


def search_first_name():
    pass


def search_second_name():
    pass


def search_full_name():
    pass


def search_phone_number():
    pass


def search_city():
    pass


def del_record_by_phone():
    pass


def upd_record_by_phone():
    pass


def exit_program():
    pass
