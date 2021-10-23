from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.field import field
import lab_python_fp.cm_timer as cm_timer
from lab_python_fp.process_data import process_data
from time import sleep
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]


def main():
    process_data("D:\PchProjects\Projects\lab3\data_light.json")


if __name__ == '__main__':
    main()

