import pytest

from src.processing import filter_by_state


def test_filter_by_state_normal(data_normal, filtering_result_normal):
    assert filter_by_state(data_normal) == filtering_result_normal


def test_filter_by_state_empty(data_state_empty, filtering_result_state_empty):
    assert filter_by_state(data_state_empty) == filtering_result_state_empty


def test_filter_by_state_lack_of_status_executed(data_lack_of_status_executed, filtering_result_lack_of_status_executed):
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
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(data)
    assert str(exc_info.value) == expected

# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
#       )