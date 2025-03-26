# Банковский виджет

## Описание:

**Банковский виджет** - это небольшое приложение, которое
выводит информацию о банковских операциях пользователя.

**В работе приложения используются функции:**
#### Модуль masks:
+ `get_mask_card_number()` - функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.
> #### _Пример работы функции:_  
> 7000792289606361 # входной аргумент  
> 7000 79** **** 6361 # выход функции
+ `get_mask_account()` - функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
> #### _Пример работы функции:_  
> 73654108430135874305 # входной аргумент  
> **4305 # выход функции
#### Модуль widget:
+ `mask_account_card()` - функция умеет обрабатывать информацию как о картах, так и о счетах. Функция принимает один аргумент — строку, содержащую тип и номер карты или счета, а возвращает строку с замаскированным номером.
> #### _Пример работы функции:_  
> _Пример для карты:_  
> Visa Platinum 7000792289606361 # входной аргумент
> Visa Platinum 7000 79** **** 6361 # выход функции
> _Пример для счета:_  
> Счет 73654108430135874305 # входной аргумент  
> Счет **4305 # выход функции
+ `get_date()` - функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ".
> #### _Пример работы функции:_  
> 2024-03-11T02:26:18.671407 # входной аргумент  
> 11.03.2024 # выход функции
#### Модуль processing:
+ `filter_by_state()` - функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'), а возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
> #### _Пример работы функции:_  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] # входной аргумент  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}] # выход функции со статусом по умолчанию 'EXECUTED'  
> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] # выход функции, если вторым аргументов передано 'CANCELED'
+ `sort_by_date()` - функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание), а возвращает новый список, отсортированный по дате.
> #### _Пример работы функции:_  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] # входной аргумент  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}] # выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
#### Модуль generators:
+ `filter_by_currency()` - функция фильтрует список транзакций и выдает транзакции, где валюта операции соответствует заданной
> #### _Пример работы функции:_
> [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
> {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"}] # входной аргумент  
> {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"} # выход функции
+ `transaction_descriptions()` - функция обрабатывает список транзакций и поочередно выдает описание каждой операции
> #### _Пример работы функции:_
> [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}, "description": "Перевод организации", "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
> {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}}, "description": "Перевод со счета на счет", "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"}] # входной аргумент  
> ["Перевод организации", "Перевод со счета на счет"] # выход функции
+ `card_number_generator()` - генератор номеров банковских карт
> #### _Пример работы функции:_
> 1, 5 # входными данными могут быть любые положительные числа в диапазоне от 0 до 9999999999999999  
> ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004", "0000 0000 0000 0005"] # выход функции

## Установка:

### **1. Клонируйте репозиторий:**
```shell
git clon https://github.com/Julijapy/mini-project
```
### **2. Установите зависимости:**
```shell
pip install -r requirements.txt
```

## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Тестирование:


Для тестирования проекта используется библиотека `pytest`. Чтобы запустить тесты, выполните команду:
```shell
pytest
```

Тесты покрывают следующие модули и функции:
- `masks`: функции `get_mask_card_number` и `get_mask_account`.
- `widget`: функции `mask_account_card` и `get_date`.
- `processing`: функции `filter_by_state` и `sort_by_date`.
- `generators`: функции `filter_by_currency`, `transaction_descriptions`, `card_number_generator`.

Покрытие тестами составляет 100% кода проекта.

## Документация:

Для получения дополнительной информации пройдите по ссылке [документация](https://gist.github.com/Jekins/2bf2d0638163f1294637)

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://web.mit.edu/) ![alt текст](https://en.wikipedia.org/wiki/MIT_License#/media/File:MIT_logo.svg)
