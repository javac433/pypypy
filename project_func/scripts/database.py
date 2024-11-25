data = {}


def check(table_name):
    return (data.get(table_name) is not None)


def create(table_name, *columns):
    data[table_name] = list(columns)


def delete(table_name):
    if check(table_name):
        del data[table_name]
        return 0
    else:
        return 1


def select(table_name):
    if table_name == "*":
        return data
    if check(table_name):
        return data[table_name]
    return 1
