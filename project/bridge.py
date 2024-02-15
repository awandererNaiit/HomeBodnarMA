import json
import pathlib


def load_operation(filename):
    """функция открывает json файл для чтения"""
    BASE_DIR = pathlib.Path(__file__).parent.parent
    filename = BASE_DIR / 'data/bank_operation.json'
    with open(filename, 'r', encoding='utf8') as f:
        information = json.load(f)
        return information


def sort_operation(operations):
    """Функция проверяет дату и фильтрует от самой новой к самой старой"""
    if operations:
        return sorted(operations, key=lambda operation: operation.get('date', ''),  reverse=True)
    return operations


def filter_operations(operations):
    """Проверяет файл по нужному нам ключу и отсеиваем лишниее
    и добавляет в список"""
    desired_state = 'EXECUTED'
    filtered_operations = []
    for operation in operations:
        if operation.get('state') == desired_state:
            filtered_operations.append(operation)
    return filtered_operations


def formatter_date(date):
    """Переписываем дату в нужный формат"""
    date = date.split('T')[0].split('-')
    formatted_date = '.'.join(date)
    return formatted_date


def formatter_from(number_from):
    """Скрываем данные пользователя и проверяем откуда была сделана операция"""

    if number_from is None:
        return 'Пополнение вклада' #или если хотим оставить значение пустым ''

    if len(number_from) == 25:
        number_from = number_from.split()
        name_card = ' '.join(number_from[:1])
        return f'{name_card} **{number_from[-1][16:20]}'

    number_from = number_from.split()
    result = len(number_from) - 1
    name_card = ' '.join(number_from[:result])
    return f'{name_card} {number_from[-1][0:4]} {number_from[-1][4:6]}** **** {number_from[-1][12:16]}'


def formatter_to(number_to):
    """Скрываем данные счета для поступления и проверем куда поступил перевод"""
    if len(number_to) == 25:
        number_to = number_to.split()
        name_card = ' '.join(number_to[:1])
        return f'{name_card} **{number_to[-1][16:20]}'

    number_to = number_to.split()
    result = len(number_to) - 1
    name_card = ' '.join(number_to[:result])
    return f'{name_card} {number_to[-1][0:4]} {number_to[-1][4:6]}** **** {number_to[-1][12:16]}'



