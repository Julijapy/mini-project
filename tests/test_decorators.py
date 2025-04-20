import os
import tempfile

import pytest

from src.decorators import log


def test_log():
    """Тестирование декоратора при возврате результата функции"""

    @log()
    def add_numbers(a, b):
        """Функция сложения"""
        return a + b

    result = add_numbers(2, 3)
    assert result == 5


def test_log_info_out(capsys):
    """Тестирование декоратора при выводе логируемой информации в консоль при отсутствии ошибок"""

    @log()
    def add_numbers(a, b):
        """Функция сложения"""
        return a + b

    add_numbers(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers ok\n"


def test_log_err():
    """Тестирование декоратора при возврате ошибки"""

    @log()
    def division(a, b):
        """Функция деления"""
        return a / b

    with pytest.raises(ZeroDivisionError):
        division(1, 0)


def test_log_err_out(capsys):
    """Тестирование декоратора при выводе логируемой информации в консоль с ошибкой"""

    @log()
    def division(a, b):
        """Функция деления"""
        return a / b

    with pytest.raises(ZeroDivisionError):
        division(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "division error: ZeroDivisionError. Inputs: (1, 0), {}\n"


def test_log_to_file():
    """Тестирование декоратора при записи логируемой информации в файл txt без ошибок"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    @log(filename=filename)
    def test_func(x, y):
        """Функция сложения"""
        return x + y

    test_func(1, 1)

    with open(filename) as f:
        content = f.read()

    os.unlink(filename)
    assert "test_func ok" in content


def test_log_to_file_err():
    """Тестирование декоратора при записи логируемой информации в файл txt с ошибкой"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    @log(filename=filename)
    def test_func(x, y):
        """Функция деления"""
        return x / y

    with pytest.raises(ZeroDivisionError):
        test_func(1, 0)

    with open(filename) as f:
        content = f.read()

    os.unlink(filename)

    assert "test_func error: ZeroDivisionError. Inputs: (1, 0), {}" in content
