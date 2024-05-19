from utils import (read_json_file, data_time_information, last_five_operations, sorted_last_five_operation, encrypys_number)

# Код для операций:
list_main = sorted_last_five_operation(
    last_five_operations(read_json_file("operations.json"), data_time_information(read_json_file("operations.json"))))
for every in list_main:
    try:
        date = every["date"].strftime("%d.%m.%Y")
        desc = every["description"]
        from_who = encrypys_number(every.get("from", ""))
        to_who = encrypys_number(every["to"])
        sum_oper = every["operationAmount"]["amount"]
        currency = every["operationAmount"]["currency"]["name"]
        print(f"""{date} {desc}
{from_who} -> {to_who}
{sum_oper} {currency}
""")
    except KeyError:
        continue
