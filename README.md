# Банковский виджет

## Описание:

**Банковский виджет** - это небольшое приложение, которое
выводит информацию о банковских операциях пользователя.

**В работе приложения используются функции:**
+ `get_mask_card_number()` - функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами.
> #### _Пример работы функции:_  
> 7000792289606361 # входной аргумент  
> 7000 79** **** 6361 # выход функции
+ `get_mask_account()` - функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
> #### _Пример работы функции:_  
> 73654108430135874305 # входной аргумент  
> **4305 # выход функции
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
+ `filter_by_state()` - функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'), а возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
> #### _Пример работы функции:_  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] # входной аргумент  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}] # выход функции со статусом по умолчанию 'EXECUTED'  
> [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] # выход функции, если вторым аргументов передано 'CANCELED'
+ `sort_by_date()` - функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание), а возвращает новый список, отсортированный по дате.
> #### _Пример работы функции:_  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] # входной аргумент  
> [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}] # выход функции (сортировка по убыванию, т. е. сначала самые последние операции)

## Установка:

### **1. Клонируйте репозиторий:**
```shell
git clon https://github.com/Julijapy/mini-project
```
### **2. Установите зависимости:**
```commandline
pip install -r requirements.txt
```

## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Создайте новый проект и начните добавлять задачи.
3. Назначайте сроки выполнения и приоритеты для задач, чтобы эффективно управлять проектами.

## Документация:

Для получения дополнительной информации пройдите по ссылке [документация](https://gist.github.com/Jekins/2bf2d0638163f1294637)

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://web.mit.edu/) ![alt текст](https://en.wikipedia.org/wiki/MIT_License#/media/File:MIT_logo.svg)
