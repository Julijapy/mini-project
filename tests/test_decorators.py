import pytest

from src.decorators import log


def test_log():
    """ Тестирование декоратора при возврате результата функции"""
    @log()
    def add_numbers(a, b):
        return a + b
    result = add_numbers(2, 3)
    assert result == 5


def test_log_info_out(capsys):
    """ Тестирование декоратора при выводе логируемой информации в консоль при отсутствии ошибок"""
    @log()
    def add_numbers(a, b):
        return a + b
    add_numbers(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"


def test_log_err():
    """ Тестирование декоратора при возврате ошибки"""
    @log()
    def division(a, b):
        return a / b
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


def test_log_err_out(capsys):
    """ Тестирование декоратора при выводе логируемой информации в консоль с ошибкой"""
    @log()
    def division(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        division(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "division error: ZeroDivisionError. Inputs: (1, 0), {}\n"
