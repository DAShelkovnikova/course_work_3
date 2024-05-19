# Тесты функций pytest:
import datetime
import os
import pytest
from project.utils import (read_json_file, data_time_information,
                             last_five_operations, sorted_last_five_operation,
                             encrypys_number)


@pytest.fixture
def test_function():
    return os.path.join("..", "project", "operations.json")


def test_read_json_file():
    assert read_json_file("test.json") == [
        {
            "pk": 4,
            "full_name": "Bauer Adkins",
            "skills": ["HTML", "CSS", "JavaScript", "React", "Node.js"]
        }
    ]


def test_data_time_information(test_function):
    assert data_time_information(read_json_file(test_function)) == [datetime.datetime(2019, 11, 5, 12, 4, 13, 781725),
                                                      datetime.datetime(2019, 11, 13, 17, 38, 4, 800051),
                                                      datetime.datetime(2019, 11, 19, 9, 22, 25, 899614),
                                                      datetime.datetime(2019, 12, 7, 6, 17, 14, 634890),
                                                      datetime.datetime(2019, 12, 8, 22, 46, 21, 935582)]


def test_last_five_operations(test_function):
    assert last_five_operations(read_json_file(test_function), data_time_information(read_json_file(test_function))) == [
        {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
        {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
         'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
        {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
         'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
        {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'},
        {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
         'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
         'to': 'Счет 46765464282437878125'}]


def test_sorted_last_five_operation(test_function):
    assert sorted_last_five_operation(last_five_operations(read_json_file(test_function), data_time_information(read_json_file(test_function)))) == [
        {'id': 863064926, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 12, 8, 22, 46, 21, 935582),
         'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
        {'id': 114832369, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 12, 7, 6, 17, 14, 634890),
         'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
         'to': 'Счет 35158586384610753655'},
        {'id': 154927927, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 11, 19, 9, 22, 25, 899614),
         'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
        {'id': 482520625, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 11, 13, 17, 38, 4, 800051),
         'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
         'to': 'Счет 46765464282437878125'},
        {'id': 801684332, 'state': 'EXECUTED', 'date': datetime.datetime(2019, 11, 5, 12, 4, 13, 781725),
         'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}},
         'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]


def test_encrypys_number():
    assert encrypys_number("Счет 48894435694657014368") == "Счет **4368"
    assert encrypys_number("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert encrypys_number("Maestro 3928549031574026") == "Maestro 3928 54** **** 4026"
    assert encrypys_number("") == ""
