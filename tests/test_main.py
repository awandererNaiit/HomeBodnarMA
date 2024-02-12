from project.main import operation
import pathlib


def test_operation():
    test_filtred_operation = [
        {
            "id": 509645757,
            "state": "EXECUTED",
            "date": "2019-10-30T01:49:52.939296",
            "operationAmount": {
                "amount": "23036.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 7756673469642839",
            "to": "Счет 48943806953649539453"
        }]

    expected_results = ['2019.10.30 Перевод с карты на счет\nVisa Gold 7756 67** **** 2839 -> Счет **9453\n23036.03 '
                        'руб.']
    assert operation(test_filtred_operation) == expected_results
