from src.generators import filter_by_currency

def test_filter_by_currency(transactions, filter_by_currency_result):
    """Тестирование функции при стандартных данных"""
    assert filter_by_currency(transactions) == filter_by_currency_result
