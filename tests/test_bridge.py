from project.bridge import load_operation, sort_operation, filter_operations, formatter_date, formatter_from, formatter_to
import json
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
filename = BASE_DIR / 'data/bank_operation.json'


def test_load_operation():
    with open(filename, 'r', encoding='utf8') as f:
        test = json.load(f)
    result = load_operation(filename)
    assert result == test


def test_sort_operation():
    operations = [{'date': '2022-01-15'}, {'date': '2022-01-10'}, {'date': '2022-01-20'}]
    sorted_operations = sort_operation(operations)
    assert sorted_operations == [{'date': '2022-01-20'}, {'date': '2022-01-15'}, {'date': '2022-01-10'}]


def test_filter_operations():
    operations = [
        {'state': 'EXECUTED', 'from': 'Maestro 1913883747791351'},
        {'state': 'CANCELED', 'from': 'Visa Platinum 1813166339376336'}
    ]
    expected_result = [
        {'state': 'EXECUTED', 'from': 'Maestro 1913883747791351'},
    ]
    assert filter_operations(operations) == expected_result


def test_formatter_date():
    input_date = '2021-10-15T12:30:45'
    expected_output = '2021.10.15'
    output = formatter_date(input_date)
    assert output == expected_output


def test_formatter_from():
    card_info = 'Visa Platinum 1813166339376336'
    assert formatter_from(card_info) == 'Visa Platinum 1813 16** **** 6336'
    card_info = 'Счет 48943806953649539453'
    assert formatter_from(card_info) == 'Счет **9453'
    card_info = 'Maestro 1913883747791351'
    assert formatter_from(card_info) == 'Maestro 1913 88** **** 1351'


def test_formatter_to():
    card_info = 'Visa Platinum 1813166339376336'
    assert formatter_to(card_info) == 'Visa Platinum 1813 16** **** 6336'
    card_info = 'Счет 48943806953649539453'
    assert formatter_to(card_info) == 'Счет **9453'
    card_info = 'Maestro 1913883747791351'
    assert formatter_to(card_info) == 'Maestro 1913 88** **** 1351'
