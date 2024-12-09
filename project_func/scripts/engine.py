#!/usr/env/python3

from .database import create_t, check, delete_t
from .database_crud import create, read, update, delete, info
import prompt


def help():
    print('Функции:\n<command> create_t table_name col_names - ', end='')
    print('''создать таблицу table_name со следующими столбцами col_names
<command> check table_name - проверить на наличие такой таблицы table
<command> delete_t table_name - удалить таблицу table_name''')
    print('''<command> create table_name data- создать запись в таблице
          table_name  со следующими значениями data
<command> read table_name col_name data- вывести значения data столбцов col_name  таблицы table_name
<command> update table_name data_old data_new- обновить значения data_new  строки со значениями data_old таблицы table_name
<command> delete table_name data - удалить строку в таблице table_name со следующими значениями data
<command> info table_name - вывести информацию о  table_name: название таблицы, количество столбцов, название столбцов
<command> exit - выход из программы
<command> help- справочная информация
''')


def check_args(args):
    if not all((i.isalpha() or i.isdigit()) for i in args):
        return "Empty or not-alphanumeric column names are not allowed"
    if len(list(set(args))) != len(args):
        return "All column names must be unique"
    return 0


def main():
    print('***База данных***')
    help()
    while True:
        command = prompt.string("Введите команду > ")
        cmd = command.split()
        length = len(cmd)
        if cmd[0] == 'create_t':
            if length == 3:
                args = cmd[2].split(',')
                if not check_args(args):
                    if "ID" not in args:
                        args.insert(0, "ID")
                    if check(cmd[1]):
                        print(f"Table {cmd[1]} already exists")
                    else:
                        create_t(cmd[1], args)
                        print(f"Created table {cmd[1]} with columns: {args}")
                else:
                    print(check_args(args))
            elif length < 3:
                print("Arguments needed")
            else:
                print("No spaces allowed between arguments")
        elif cmd[0] == 'check':
            if length != 2:
                print("Syntax incorrect")
            elif check(cmd[1]):
                print(f"Table \'{cmd[1]}\' exists")
            else:
                print(f"Table \'{cmd[1]}\' does not exist")
        elif cmd[0] == 'delete_t':
            if length != 2:
                print('Syntax incorrect')
            elif check(cmd[1]):
                delete_t(cmd[1])
                print(f"Table \'{cmd[1]}\' deleted")
            else:
                print(f"Table \'{cmd[1]}\' does not exist")
        elif cmd[0] == 'help':
            help()
        elif cmd[0] == 'exit':
            exit(0)
        elif cmd[0] == 'create':
            if len(cmd) < 3:
                print("Too few arguments")
            elif len(cmd) > 3:
                print("Too many args")
            else:
                t = create(cmd[1], cmd[2])
                if t == "ERR_FEW_ARGS":
                    print("More arguments are required")
                elif t == "ERR_MANY_ARGS":
                    print("Too many arguments")
        elif cmd[0] == 'read':
            if len(cmd) < 3:
                print("Too few arguments")
            else:
                print(read(cmd[1], cmd[2], cmd[3:]))
        elif cmd[0] == 'update':
            if len(cmd) < 4:
                print("Too few arguments")
            else:
                t = update(cmd[1], cmd[2], cmd[3:])
                if t == "ERR_NO_FIELD":
                    print("No fields to update are specified")
        elif cmd[0] == 'delete':
            if len(cmd) < 3:
                print("Too few arguments")
            else:
                t = delete(cmd[1], cmd[2:])
                if t == "ERR_NO_DATA":
                    print("No data for removal is specified")
                elif isinstance(t, list):
                    print("One of the arguments is extra: ", t[0])
        elif cmd[0] == 'info':
            if len(cmd) < 2:
                print("Specify table name")
            else:
                t = info(cmd[1])
                print(f"Table name: {t['tn']}, columns amount: {t['ca']}, columns: {t['cols']}")
        else:
            print("Command incorrect")


if __name__ == '__main__':
    main()
