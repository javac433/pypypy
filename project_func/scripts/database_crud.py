from prettytable import PrettyTable
import csv
from .database import check


def get_cols(table_name):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    with open(f'./database/{table_name}.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            return list(row)


def get_last_id(table_name):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    rows = []
    with open(f'./database/{table_name}.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    if rows[-1][0].isdigit():
        return int(rows[-1][0])
    return 0


def create(table_name, args):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    args = [str(get_last_id(table_name) + 1)] + args.split(',')
    amnt = len(get_cols(table_name))
    if len(args) < amnt:
        return "ERR_FEW_ARGS"
    elif len(args) > amnt:
        return "ERR_MANY_ARGS"
    with open(f'./database/{table_name}.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(args)
    return "ERR_OK"


def read(table_name, cols, data):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    table = PrettyTable()
    COLS_C = get_cols(table_name)
    table.field_names = COLS_C
    if data is not None:
        data_load = {k.split('=')[0]: k.split('=')[1] for k in data}
    else:
        data_load = {}
    with open(f"./database/{table_name}.csv") as file:
        reader = csv.reader(file)
        first = 0
        for row in reader:
            if not first:
                first = 1
                continue
            if data_load != {}:
                for i in range(len(COLS_C)):
                    if data_load.get(COLS_C[i]) is not None:
                        if data_load[COLS_C[i]] == row[i]:
                            table.add_row(row)
                            break
            else:
                table.add_row(row)
    if cols == '*':
        return table.get_string()
    return table.get_string(fields=cols.split(','))


def update(table_name, data_old: str, data_new: list):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    old = data_old.split('=')
    rows = []
    cols = get_cols(table_name)
    if old[0] not in cols or data_new[0][0] not in cols:
        return "ERR_NO_FIELD"
    with open(f"./database/{table_name}.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ind1 = cols.index(old[0])
            for elem in data_new:
                new = elem.split('=')
                ind2 = cols.index(new[0])
                if row[ind1] == old[1]:
                    row[ind2] = new[1]
            rows.append(row)
    with open(f"./database/{table_name}.csv", 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
    return "ERR_OK"


def delete(table_name, data):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    rows = []
    if len(data) == 0:
        return "ERR_NO_DATA"
    data_load = {k.split('=')[0]: k.split('=')[1] for k in data}
    cols = get_cols(table_name)
    with open(f'./database/{table_name}.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for t in data_load:
                if t not in cols:
                    return [t]
                if row[cols.index(t)] != data_load[t]:
                    rows.append(row)

    with open(f'./database/{table_name}.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)

    return "ERR_OK"


def info(table_name):
    if check(table_name) == 0:
        print("Table name is incorrect")
        return
    return {'tn': table_name, 'ca': len(get_cols(table_name)),
            'cols': get_cols(table_name)}
