import prompt


def welcome():
    while True:
        res = prompt.string('Введите команду: ')
        if res == 'exit':
            print('До свидания')
            exit(0)
        elif res == 'help':
            print('***\n<command> exit - выйти из программы\n')
            print('<command> help - справочная информация')
