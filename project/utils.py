# Импортируем модули:
import json
import datetime


# Функции:
def read_json_file(name):
    """Берет данные из json файла"""
    with open(name, "r") as file:
        data = json.load(file)
    return data


def data_time_information(operation_date):
    """Возвращает информацию о дате и времени последних 5 операций"""
    date_of_operation = []
    for operations in operation_date:
        try:
            if operations["state"] == "EXECUTED":
                date_of_operation.append(datetime.datetime.fromisoformat(operations["date"]))
        except KeyError:
            continue
    return sorted(date_of_operation)[-5:]


def last_five_operations(list_operations, last_five_datetime):
    """Возвращает информацию о последних 5 операциях"""
    last_five = []
    for operation in list_operations:
        try:
            if datetime.datetime.fromisoformat(operation["date"]) in last_five_datetime:
                last_five.append(operation)
        except KeyError:
            continue
    return last_five


def sorted_last_five_operation(last_five_operations):
    """Сортирует последние 5 операций в порядке убывания начиная с последней"""
    last_five = last_five_operations
    for every in last_five:
        every["date"] = datetime.datetime.fromisoformat(every["date"])
    sorted_last_five = sorted(last_five, key=lambda x: x["date"], reverse=True)
    return sorted_last_five


def encrypys_number(string_number):
    """Шифрует информацию о номере счета"""
    text_list = string_number.split()
    try:
        replace_number = ", ".join(([text_list[-1][length:length + 4] for length in range(0, len(text_list[-1]), 4)]))
    except IndexError:
        return ""
    replace_number_min = replace_number.replace(",", "")
    if text_list[0] != "Счет":
        replace_number_finally = replace_number_min[:7] + "** ****" + replace_number_min[-5:]
    else:
        replace_number_finally = "**" + replace_number_min[-4:]
    text_list_replace = text_list[:-1]
    text_list_replace.append(replace_number_finally)
    text_replace = ", ".join(text_list_replace).replace(",", "")
    return text_replace
