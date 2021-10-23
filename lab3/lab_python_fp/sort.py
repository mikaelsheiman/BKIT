from operator import itemgetter


def sort1(data):
    return [data[i] for i, item in sorted(enumerate([abs(item) for item in data]), key=itemgetter(1), reverse=True)]


def sort2(data, reverse=False):
    return sorted(data, key=lambda x: abs(x), reverse=reverse)

