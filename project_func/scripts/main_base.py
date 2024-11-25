#!/usr/bin/env python3

from .. import cli


def main():
    print('Первая попытка запустить проект!')
    print('***\n<command> exit - выйти из программы\n')
    print('<command> help - справочная информация')
    cli.welcome()


if __name__ == '__main__':
    main()
