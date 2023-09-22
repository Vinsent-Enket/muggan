import json
from pathlib import Path

from src.utils.tools import time_converter, mask_maker

file_path = Path("../../material/operations.json")
file = open(file_path)
operations = json.load(file)


last_operation = [
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"},
    {"date": "2009-12-24T20:16:18.819037"}
]


def re_write(operation):
    for i in range(4):
        if time_converter(last_operation[i]["date"]) < time_converter(operation["date"]):
            last_operation.insert(i, operation)
            last_operation.pop()

            break
"""def re_write(operation):
    for i in range(5):
        print(i)
        if last_operation[i]["date"] < operation["date"]:
            print(f"сравнивали {last_operation[i]['date']} и {operation['date']}")
            last_operation[i] = operation

            break"""

def statistic_out(list_op):
    for i in list_op:
        print(i, "\n")

for operation in operations:
    if "state" in operation and operation["state"] == "EXECUTED":
            re_write(operation)


print(last_operation)
itog = mask_maker(last_operation)

statistic_out(itog)

