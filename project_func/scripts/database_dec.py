import csv
import time
import os

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        res = end_time - start_time
        print(f"Время выполнения: {res} секунд")
        return result
    return wrapper


def check_uniqueness(func):
    def wrapper(*args, **kwargs):
        if f'{args[0]}.csv' not in os.listdir('./database'):
            return None
        with open(f'./database/{args[0]}.csv', 'r') as table:
            found = False
            reader = csv.reader(table)
            for row in reader:
                found = any(','.join(args[1:]) in ','.join(row) for row in reader)
            
            if found:
                print(f"Строка \'{''.join(args[1:])}\' уже есть в таблице.")
                return func(*args, **kwargs)
            print(f"Строки \'{''.join(args[1:])}\' нет в таблице.")
            return func(*args, **kwargs)
    return wrapper

def confirm_action(func):
    def wrapper(*args, **kwargs):
        confirmation = input(f"Вы уверены, что хотите выполнить {func.__name__}: ?")
        if confirmation in ('yes', 'y'):
            print("Продолжаю...")
            return func(*args, **kwargs)
        else:
            print("Действие отменено.")
            return None

    return wrapper


