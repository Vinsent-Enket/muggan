import json
from pathlib import Path
from src.utils.tools import time_converter, mask_maker

"""
Чтобы не терялся путь к файлу использовал модуль патхлиб, затем создал заготовку с заранее созданными словарями,
но можно было просто сначала заполнить их первыми попавшимися из файла
"""

file_path = Path("../material/operations.json")
file = open(file_path)
operations = json.load(file)



last_operation = [
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"}
]

"""
перебираем операции из полученного файла, отсекаем все что не executed затем провереям с last_operation
Полученный список маскируем функцией и выводим в консоль
"""

for operation in operations:
    if "state" in operation and operation["state"] == "EXECUTED":
            for i in range(4):
                if time_converter(last_operation[i]["date"]) < time_converter(operation["date"]):
                    last_operation.insert(i, operation)
                    last_operation.pop()
                    break

result = mask_maker(last_operation)

for data_string in result:
    print(data_string, "\n")

