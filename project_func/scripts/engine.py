#!/usr/env/python3

from .database import create, check, delete, select
import prompt


def help():
    print('Функции:\n<command> create table_name col_names - ', end='')
    print('''создать таблицу table_name со следующими столбцами col_names
<command> check table_name - проверить на наличие такой таблицы table
<command> delete table_name - удалить таблицу table
<command> exit - выход из программы
<command> help - справочная информация
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
        if cmd[0] == 'create':
            if length == 3:
                args = cmd[2].split(',')
                if not check_args(args):
                    if "ID" not in args:
                        args.insert(0, "ID")
                    if check(cmd[1]):
                        print(f"Table {cmd[1]} already exists")
                    else:
                        create(cmd[1], args)
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
        elif cmd[0] == 'delete':
            if length != 2:
                print('Syntax incorrect')
            elif check(cmd[1]):
                delete(cmd[1])
                print(f"Table \'{cmd[1]}\' deleted")
            else:
                print(f"Table \'{cmd[1]}\' does not exist")
        elif cmd[0] == 'help':
            help()
        elif cmd[0] == 'exit':
            exit(0)
        elif cmd[0] == 'select':
            if select(cmd[1]) == 1:
                print(f"Table \'{cmd[1]}\' does not exist")
            else:
                print(select(cmd[1]))
        else:
            print("Command incorrect")


if __name__ == '__main__':
    main()
