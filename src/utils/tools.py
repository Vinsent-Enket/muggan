import datetime


def time_converter(datetime_string):
    """
    используя библиотеку дататайм конвертируем строковое значение в тип время и убираем микросекунд
    :param datetime_string:
    :return:
    """

    datetime_obj = datetime.datetime.strptime(datetime_string[:-7], '%Y-%m-%dT%H:%M:%S')
    #print(f"//////////////из {datetime_string} получилось {datetime_obj}/////////////////////")
    return datetime_obj
def mask_maker(last_operation):
    """
    получаем на вход список из 5ти последних операций и преобразуем их
    Можно было бы не делать единую строку, а разбить их по отдельности, тогда и тест было бы сделать на 100 проц
    :param last_operation:
    :return:
    """
    mask_operation = []

    for choice_operation in last_operation:
        key_kard_from = ""
        key_numb_from = ""
        key_kard_to = ""
        key_numb_to = ""
        description = choice_operation['description']
        date = time_converter(choice_operation['date'])
        summ = choice_operation["operationAmount"]["amount"] + " " + choice_operation["operationAmount"]["currency"]["name"]
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
        mask_operation.append(f"Дата - {date}, тип операции - {description}, "
                              f"Откуда {key_kard_from} {key_numb_from} "
                              f"Куда {key_kard_to} {key_numb_to} "
                              f"сумма -  {summ}")

    return mask_operation

