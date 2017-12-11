# Ближайшие бары

Программа получает на вход файл в формате json, в котором содержатся данные о барах. Программа находит самый большой и маленький бар, а также самый близкий бар исходя из введенных долготы и широты. 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```
$ python bars.py [название_файла_с_данными.txt]
```

example output
```

Самый большой бар:  Спорт бар «Красная машина»
Количество мест:  450
Адрес:  Автозаводская улица, дом 23, строение 1
Телефон:  (905) 795-15-84

Самый маленький бар:  БАР. СОКИ
Количество мест:  0
Адрес:  Дубравная улица, дом 34/29
Телефон:  (495) 258-94-19

Введите вашу долготу: 57.76543
Введите вашу широту: 37.87654
Самый ближайший бар:  Таверна
Количество мест:  16
Адрес:  проспект Защитников Москвы, дом 8
Телефон:  (977) 511-73-23
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
