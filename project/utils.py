import json
import datetime


# Функции:
def read_json_file(name):
    """Берет данные из json файла"""
    with open(name, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_executed_operations(operations):
    """Возвращает список операций с состоянием EXECUTED"""
    executed_operations = []
    for operation in operations:
        if operation.get("state") == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_sorted_operations(operations):
    """Возвращает отсортированный списаок операций по дате"""
    for every in operations:
        every["date"] = datetime.datetime.fromisoformat(every["date"])
    sorted_operations = sorted(operations, key=lambda x: x["date"], reverse=True)
    return sorted_operations


def get_five_operations(list_operations):
    """Возвращает список из последних 5 операций"""
    return list_operations[:5]


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
