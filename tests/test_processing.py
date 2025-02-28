import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_normal(data_normal, filtering_result_normal):
    """ Тестирование функции при стандартных данных"""
    assert filter_by_state(data_normal) == filtering_result_normal


def test_filter_by_state_empty(data_state_empty, filtering_result_state_empty):
    """ Тестирование функции при пустых значениях 'state'"""
    assert filter_by_state(data_state_empty) == filtering_result_state_empty


def test_filter_by_state_lack_of_status_executed(data_lack_of_status_executed, filtering_result_lack_of_status_executed):
    """ Тестирование функции при отсутствующем статусе 'EXECUTED'"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(data_lack_of_status_executed)
    assert str(exc_info.value) == filtering_result_lack_of_status_executed


@pytest.mark.parametrize("data, expected", [([{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}],
                                             [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                            ([{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
                                              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                              {'id': 594226727, 'state': '', 'date': '2018-09-12T21:27:25.241689'},
                                              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                             [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_filter_by_state_with_different_data(data, expected):
    """ Тестирование функции при разных данных 'state'"""
    assert filter_by_state(data) == expected


@pytest.mark.parametrize("data, expected", [([{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
                                              {'id': 939719570, 'state': '', 'date': '2018-06-30T02:08:58.425572'},
                                              {'id': 594226727, 'state': '', 'date': '2018-09-12T21:27:25.241689'}],
                                              "Список пуст"),
                                            ([{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
                                              {'id': 939719570, 'state': '', 'date': '2018-06-30T02:08:58.425572'},
                                              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                              {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}],
                                              "Список пуст")])
def test_filter_by_state_no_executed(data, expected):
    """ Тестирование функции filter_by_state с отсутствующим значением 'EXECUTED'"""
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(data)
    assert str(exc_info.value) == expected


def test_sort_by_date_normal(data_normal, sort_by_date_result_normal):
    """ Тестирование функции при стандартных данных при reverse=True по умолчанию"""
    assert sort_by_date(data_normal) == sort_by_date_result_normal


def test_sort_by_date_increasing(data_normal, sort_by_date_increasing):
    """ Тестирование функции при стандартных данных при reverse=False"""
    assert sort_by_date(data_normal, False) == sort_by_date_increasing


def test_sort_by_date_with_the_same_dates(same_dates, sort_result_same_dates):
    """ Тестирование функции при входящих данных с одинаковыми датами"""
    assert sort_by_date(same_dates) == sort_result_same_dates


def test_sort_by_date_list_empty(date_empty, filtering_result_lack_of_status_executed):
    """ Тестирование функции при входящих данных с пустым списком"""
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(date_empty)
    assert str(exc_info.value) == filtering_result_lack_of_status_executed


@pytest.mark.parametrize("date_value_empty, expected",[([{'id': 41428829, 'state': 'EXECUTED'},
                                                   {'id': 939719570, 'state': 'EXECUTED', 'date': ''},
                                                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                                  [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}])])
def test_sort_by_date_empty_date(date_value_empty, expected):
    """ Тестирование функции с пустым значением 'date'"""
    assert sort_by_date(date_value_empty) == expected


@pytest.mark.parametrize("format_incorrect, expected", [([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019/07/03T18:35:29.512364'},
                                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30'},
                                                          {'id': 41428829, 'state': 'EXECUTED', 'date': '2019'},
                                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018.06.30'},
                                                          {'id': 594226727, 'state': 'CANCELED', 'date': 'abcabcabcabc'},
                                                          {'id': 615064591, 'state': 'CANCELED', 'date': '123123123123123123123'},
                                                          {'id': 41428829, 'state': 'EXECUTED', 'date': ' '},
                                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-6-30T02:08:58.425572'},
                                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                                                         [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30'}])])
def test_sort_by_date_format_incorrect(format_incorrect, expected):
    """ Тестирование функции при частично некорректных значениях 'date'"""
    assert sort_by_date(format_incorrect) == expected


def test_sort_by_date_all_incorrect_value(date_all_value_incorrect, filtering_result_lack_of_status_executed):
    """ Тестирование функции при некорректных значениях 'date'"""
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(date_all_value_incorrect)
    assert str(exc_info.value) == filtering_result_lack_of_status_executed
