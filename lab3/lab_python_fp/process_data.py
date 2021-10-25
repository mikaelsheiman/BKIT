import random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1 as timer
import json


@print_result
def f1(data):
    return list(Unique(sorted([items["job-name"] for items in data]), ignore_case=True))


@print_result
def f2(data):
    return list(filter(lambda x: str(x).lower().find("программист") != -1, data))


@print_result
def f3(data):
    return [item + " с опытом работы в Python" for item in data]


@print_result
def f4(data):
    return [str(item) + '. Зарплата {} руб.'.format(str(int(random.random() * 100000 + 100000))) for item in data]


def process_data(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    with timer():
        f4(f3(f2(f1(data))))
