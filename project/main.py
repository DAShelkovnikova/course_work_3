
from utils import get_executed_operations, read_json_file, get_sorted_operations, get_five_operations, encrypys_number

# Код для операций:

operations = read_json_file("operations.json")
executed_operations = get_executed_operations(operations)
sorted_operations = get_sorted_operations(executed_operations)
five_operations = get_five_operations(sorted_operations)
for every in five_operations:
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


