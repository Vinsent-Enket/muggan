import datetime


def time_converter(datetime_string):
    """
    используя библиотеку дататайм конвертируем строковое значение в тип время и убираем микросекунды
    :param datetime_string:
    :return:
    """

    datetime_obj = datetime.datetime.strptime(datetime_string[:-7], '%Y-%m-%dT%H:%M:%S')
    #print(f"//////////////из {datetime_string} получилось {datetime_obj}/////////////////////")
    return datetime_obj
def mask_maker(last_operation):
    """
    получаем на вход список из 5ти последних операций и преобразуем их
    :param last_operation:
    :return:
    """
    mask_operation = []

    for choice_operation in last_operation:
        key_kard_from = ""
        key_numb_from = ""
        key_kard_to = ""
        key_numb_to = ""
        date = time_converter(choice_operation['date'])
        if 'from' in choice_operation:
            for letter in choice_operation['from']:
                if not letter.isdigit():
                    key_kard_from += letter
                else:
                    key_numb_from += letter
            key_numb_from = key_numb_from[:2] + " ** " * 3 + key_numb_from[-4:]
        if 'to' in choice_operation:
            for letter in choice_operation['to']:
                if not letter.isdigit():
                    key_kard_to += letter
                else:
                    key_numb_to += letter
            key_numb_to = key_numb_to[:2] + " ** " * 3 + key_numb_to[-4:]
        mask_operation.append(f"Дата - {date}, тип операции - {choice_operation['description']}, "
                              f"Откуда {key_kard_from} {key_numb_from} "
                              f"Куда {key_kard_to} {key_numb_to} ")

    return mask_operation
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
print(mask_maker(test_dict))
