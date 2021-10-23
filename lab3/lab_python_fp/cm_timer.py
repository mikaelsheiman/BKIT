from time import time as tm
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = tm()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('time: {}'.format(tm() - self.start_time))


@contextmanager
def cm_timer_2():
    start_time = tm()
    yield
    print('time: {}'.format(tm() - start_time))
