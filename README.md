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
Самый большой бар:
{
 "geometry": {
  "coordinates": [
   37.638228501070095,
   55.70111462948684
  ],
  "type": "Point"
 },
 "properties": {
  "Attributes": {
   "Address": "Автозаводская улица, дом 23, строение 1",
   "AdmArea": "Южный административный округ",
   "District": "Даниловский район",
   "IsNetObject": "нет",
   "Name": "Спорт бар «Красная машина»",
   "OperatingCompany": null,
   "PublicPhone": [
    {
     "PublicPhone": "(905) 795-15-84"
    }
   ],
   "SeatsCount": 450,
   "SocialPrivileges": "нет",
   "global_id": 169375059
  },
  "DatasetId": 1796,
  "ReleaseNumber": 2,
  "RowId": "fbe6c340-4707-4d74-b7ca-2b84a23bf3a8",
  "VersionNumber": 2
 },
 "type": "Feature"
}
Самый маленький бар:
{
 "geometry": {
  "coordinates": [
   37.35805920566864,
   55.84614475898795
  ],
  "type": "Point"
 },
 "properties": {
  "Attributes": {
   "Address": "Дубравная улица, дом 34/29",
   "AdmArea": "Северо-Западный административный округ",
   "District": "район Митино",
   "IsNetObject": "нет",
   "Name": "БАР. СОКИ",
   "OperatingCompany": null,
   "PublicPhone": [
    {
     "PublicPhone": "(495) 258-94-19"
    }
   ],
   "SeatsCount": 0,
   "SocialPrivileges": "нет",
   "global_id": 20675518
  },
  "DatasetId": 1796,
  "ReleaseNumber": 2,
  "RowId": "17adc22c-5c41-4e4b-872f-815b521f2b53",
  "VersionNumber": 2
 },
 "type": "Feature"
}
Введите вашу долготу: 37.543
Введите вашу широту: 57.76543456
Самый ближайший бар:
{
 "geometry": {
  "coordinates": [
   37.55253288090494,
   55.9366542814469
  ],
  "type": "Point"
 },
 "properties": {
  "Attributes": {
   "Address": "9-я Северная линия, дом 3А",
   "AdmArea": "Северо-Восточный административный округ",
   "District": "район Северный",
   "IsNetObject": "нет",
   "Name": "Капитан Конрад",
   "OperatingCompany": null,
   "PublicPhone": [
    {
     "PublicPhone": "нет телефона"
    }
   ],
   "SeatsCount": 60,
   "SocialPrivileges": "нет",
   "global_id": 169376022
  },
  "DatasetId": 1796,
  "ReleaseNumber": 2,
  "RowId": "241b7aac-7895-4f15-a69b-35896dedc778",
  "VersionNumber": 2
 },
 "type": "Feature"
}
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
