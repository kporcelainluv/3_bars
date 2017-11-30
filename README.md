# Ближайшие бары

Программа анализирует список московских баров, находит самый большой и маленький бар, а также самый близкий бар исходя из введенных долготы и широты. 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```
$ python bars.py [название_файла_с_данными.txt]
```

example output
```
Самый большой бар:  {'geometry': {'coordinates': [37.638228501070095, 55.70111462948684], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': 'fbe6c340-4707-4d74-b7ca-2b84a23bf3a8', 'Attributes': {'global_id': 169375059, 'Name': 'Спорт бар «Красная машина»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Южный административный округ', 'District': 'Даниловский район', 'Address': 'Автозаводская улица, дом 23, строение 1', 'PublicPhone': [{'PublicPhone': '(905) 795-15-84'}], 'SeatsCount': 450, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Самый маленький бар:  {'geometry': {'coordinates': [37.35805920566864, 55.84614475898795], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '17adc22c-5c41-4e4b-872f-815b521f2b53', 'Attributes': {'global_id': 20675518, 'Name': 'БАР. СОКИ', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Митино', 'Address': 'Дубравная улица, дом 34/29', 'PublicPhone': [{'PublicPhone': '(495) 258-94-19'}], 'SeatsCount': 0, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
Введите долготу: 37.423433
Введите широту: 57.765433456
Самый ближайший бар:  {'geometry': {'coordinates': [37.389700176848976, 55.89739404300917], 'type': 'Point'}, 'properties': {'DatasetId': 1796, 'VersionNumber': 2, 'ReleaseNumber': 2, 'RowId': '0736ee81-9778-463d-bf2c-f6542f40e762', 'Attributes': {'global_id': 58839964, 'Name': 'Бильярд «Седьмая луза»', 'IsNetObject': 'нет', 'OperatingCompany': None, 'AdmArea': 'Северо-Западный административный округ', 'District': 'район Куркино', 'Address': 'Соколово-Мещерская улица, дом 16/114', 'PublicPhone': [{'PublicPhone': '(495) 973-67-16'}], 'SeatsCount': 25, 'SocialPrivileges': 'нет'}}, 'type': 'Feature'}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
