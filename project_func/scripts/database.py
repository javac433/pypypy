import csv
import os

if 'database' not in os.listdir():
    os.system('mkdir database')


def check(table_name):
    try:
        open(f'./database/{table_name}.csv', 'r')
    except FileNotFoundError:
        return 0
    return 1


def create_t(table_name, columns):
    with open(f'./database/{table_name}.csv', 'w') as table:
        writer = csv.writer(table)
        writer.writerow(columns)


def delete_t(table_name):
    if check(table_name):
        os.remove(f'./database/{table_name}.csv')
        return 0
    else:
        return 1
