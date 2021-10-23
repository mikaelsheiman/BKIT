import random

from lab_python_fp.unique import Unique
from lab_python_fp.sort import sort2 as sort
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1 as timer
import json
import sys


@print_result
def f1(data):
    return Unique(sorted([items["jod-name"] for items in data]), ignore_case=True)


@print_result
def f2(data):
    return filter(lambda x: str(x).lower().find("программист") == True, data)


@print_result
def f3(data):
    return [item + " с опытом работы в Python" for item in data]


@print_result
def f4(data):
    return [str(item) + str((random.random() * 100000 + 100000).as_integer_ratio()) for item in data]


def process_data(path):
    with open(path) as f:
        data = json.load(f)
    with timer():
        f4(f3(f2(f1)))
