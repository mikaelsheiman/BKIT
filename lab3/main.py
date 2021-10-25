from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.field import field
from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
from lab_python_fp.process_data import process_data
from lab_python_fp.gen_random import gen_random
from lab_python_fp.sort import sort1, sort2
from time import sleep
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black', 'some': 'some'}
]
data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(10, 1, 3)
data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']


@print_result
def test1():
    return 42


@print_result
def test2():
    return list(gen_random(10, 23, 199))


@print_result
def test3():
    d = dict()
    d[1] = 2
    d[2] = 3
    return d


def test4():
    sleep(5)


def main():
    process_data("D:\PchProjects\Projects\lab3\data_light.json")


if __name__ == '__main__':
    main()

