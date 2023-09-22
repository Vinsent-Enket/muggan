import datetime

from src.utils.tools import time_converter, mask_maker

test_dict =[{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }
]



def test_time_converter():
    assert time_converter("2048-12-24T20:16:18.819037") == datetime.datetime(2048, 12, 24, 20, 16, 18)

def test_mask_maker():
    assert mask_maker([]) == []
    assert mask_maker(test_dict) == ['Дата - 2019-12-08 22:46:21, тип операции - Открытие вклада, Откуда   Куда Счет  90 **  **  ** 5907 ']

