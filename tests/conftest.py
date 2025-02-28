import pytest


@pytest.fixture
def data_normal():
    """ Стандартные данные для входа """
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def filtering_result_normal():
    """ Результат функции filter_by_state при стандартных данных"""
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def data_state_empty():
    """ Данные на вход для функции filter_by_state с пустым ключом state"""
    return [{'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': '', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def filtering_result_state_empty():
    """ Результат для функции filter_by_state с пустым ключом state"""
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def data_lack_of_status_executed():
    """ Данные на вход для функции filter_by_state с отсутствующим значением 'EXECUTED'"""
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def filtering_result_lack_of_status_executed():
    """ Фикстура для тестирования функции с возвращаемым пустым списком"""
    return "Список пуст"


@pytest.fixture
def sort_by_date_result_normal():
    """ Результат тестирования функции sort_by_date при стандартных данных для входа"""
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def sort_by_date_increasing():
    """ Результат тестирования функции sort_by_date при reverse=False"""
    return [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]


@pytest.fixture
def date_empty():
    """ Данные для входа с пустым списком"""
    return []


@pytest.fixture
def same_dates():
    """ Данные для входа с одинаковыми датами"""
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:30.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:40.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.fixture
def sort_result_same_dates():
    """ Результат тестирования функции при входящих данных с одинаковыми датами"""
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:40.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:30.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


@pytest.fixture
def date_all_value_incorrect():
    """ Данные для входа с некорректными датами"""
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': ' '},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018 10 14'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019 July 03'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-6-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018/09/12'},
            {'id': 615064591, 'state': 'CANCELED', 'date': 'date: 2018-10-14'}]
