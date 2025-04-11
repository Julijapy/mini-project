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

