from csv import DictWriter, DictReader
from os.path import exists

print(
    'Для добавления данных нажмите - 1\n'
    'Для вывода данных в консоль нажмите - 2\n'
    'Для изменения данных нажмите - 3\n'
    'Для удаления данных нажмите - 4\n'
    'Для завершения работы программы нажмите - 5')


def create_file():  # Создание файла  и запись шапки( заголовок)
    with open("phone.csv", "w", encoding="utf-8") as data:
        f_writter = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер'])
        f_writter.writeheader()


def get_info():  # Добавление новой строки в файл  # ['иванов' 'иван', 'иванович', '123']
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, patronymic, phone_number


def show_contacts(file_name): # Показ данных в файле в консоли
    print('Вот список Ваших контактов: \n')
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
        for row in result:
            print(row['Фамилия'], row['Имя'], row['Отчество'], row['Номер'])
    return result


def write_file(file_name, lst):  # запись нового контакта
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
    obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Отчество': lst[2], 'Номер': lst[3]}
    result.append(obj)
    with open("phone.csv", "w", encoding="utf-8", newline="") as data:
        f_writter = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер'])
        f_writter.writeheader()
        f_writter.writerows(result)


def change_contact(file_name): # изменение данных контакта
    show_contacts(file_name)
    row_to_change = int(input('\nВведите номер записи для изменения или 0 для выхода: ')) - 1
    if row_to_change == -1:
        return
    changed_row = get_info()
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
    obj = {'Фамилия': changed_row[0], 'Имя': changed_row[1], 'Отчество': changed_row[2],
           'Номер': changed_row[3]}
    result[row_to_change] = obj
    with open("phone.csv", "w", encoding="utf-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(result)


def delete_contact(file_name): # удаление контакта
    show_contacts(file_name)
    row_to_delete = int(int(input('\nВведите номер записи для удаления или 0 для выхода: ')) - 1)
    if row_to_delete == -1:
        return
    with open(file_name, encoding="utf-8") as data:
        f_reader = DictReader(data)
        result = list(f_reader)
        result.pop(row_to_delete)
    with open("phone.csv", "w", encoding="utf-8", newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(result)


def main():
    while True:
        command = input("Введите команду: ")
        if command == "5":
            break
        elif command == "2":
            print(show_contacts("phone.csv"))
        elif command == "1":
            if not exists("phone.csv"):
                create_file()
            write_file("phone.csv", get_info())
        elif command == "3":
            change_contact("phone.csv")
        elif command == "4":
            delete_contact("phone.csv")


main()