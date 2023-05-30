import json
import os

phonebook_name = input('Введи назву телефонної книги: ')


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
        search_last_name()
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
    phone_number = input('Введи номер телефону: ')
    first_name = input('Введи ім`я: ')
    last_name = input('Введи прізвище: ')
    city = input('Введи назву міста: ')
    info = {
        'phone_number': phone_number,
        'first_name': first_name,
        'last_name': last_name,
        'full_name': first_name + ' ' + last_name,
        'city': city
    }
    data_dict[phone_number] = info
    with open(phonebook_name + '.json', 'w') as file:
        json.dump(data_dict, file)
    print('Контакт збережено.')
    is_another_contact = input('Додати ще один контакт? Введіть: Так або Ні. ')
    if is_another_contact == 'Так':
        add_new_entries()
    else:
        menu()


def search_first_name():
    first_name = input('Введіть ім`я для пошуку: ')
    for number, info in data_dict.items():
        for name in info.values():
            if name.lower() == first_name.lower():
                print(data_dict[number])
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        search_first_name()
    else:
        menu()


def search_last_name():
    last_name = input('Введіть прізвище для пошуку: ')
    for number, info in data_dict.items():
        for lastname in info.values():
            if lastname.lower() == last_name.lower():
                print(data_dict[number])
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        search_last_name()
    else:
        menu()


def search_full_name():
    full_name = input('Введіть повне ім`я для пошуку: ')
    for number, info in data_dict.items():
        for fullname in info.values():
            if fullname.lower() == full_name.lower():
                print(data_dict[number])
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        search_full_name()
    else:
        menu()


def search_phone_number():
    phone_number = input('Введіть номер телефону для пошуку: ')
    for number in data_dict.keys():
        if number == phone_number:
            print(data_dict[number])
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        search_phone_number()
    else:
        menu()


def search_city():
    city = input('Введіть повне ім`я для пошуку: ')
    for number, info in data_dict.items():
        for city_name in info.values():
            if city_name.lower() == city.lower():
                print(data_dict[number])
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        search_city()
    else:
        menu()


def del_record_by_phone():
    phone_number = input('Введіть номер телефону для видалення: ')
    for number in list(data_dict):
        if number == phone_number:
            data_dict.pop(number)
            print(f'Дані про контакт {number} було видалено')
    with open(phonebook_name + '.json', 'w') as file:
        json.dump(data_dict, file)
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        del_record_by_phone()
    else:
        menu()


def upd_record_by_phone():
    phone_number = input('Введіть номер телефону для зміни даних: ')
    for number, info in data_dict.items():
        if number == phone_number:
            first_name = input('Введи нове ім`я: ')
            last_name = input('Введи нове прізвище: ')
            city = input('Введи назву міста: ')
            info = {
                'first_name': first_name,
                'last_name': last_name,
                'full_name': first_name + ' ' + last_name,
                'city': city
            }
            data_dict[phone_number] = info
            print('Контакт збережено.')
    with open(phonebook_name + '.json', 'w') as file:
        json.dump(data_dict, file)
    is_repeat = input('Бажаєте повторити? Введіть: Так або Ні. ')
    if is_repeat == 'Так':
        upd_record_by_phone()
    else:
        menu()


def exit_program():
    data.close()
    print('Виконання програми завершено')


try:
    if not os.path.exists(f'{phonebook_name}.json'):
        print('Телефонної книги з такою назвою не знайдено')
        raise FileNotFoundError
    else:
        with open(phonebook_name + '.json') as data:
            data_dict = json.load(data)
        menu()
except FileNotFoundError:
    is_new_phonebook = input('Бажаєте створити? Введіть: Так або Ні. ')
    if is_new_phonebook == 'Так':
        with open(phonebook_name + '.json', 'w') as data:
            phonebook_data = dict()
            json.dump(phonebook_data, data)
        print(f'{phonebook_name}.json був створений')
        with open(phonebook_name + '.json') as data:
            data_dict = json.load(data)
        menu()
    else:
        print('Виконання програми завершено')
