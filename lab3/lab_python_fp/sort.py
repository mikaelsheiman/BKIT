
def sort1(data, reverse=False):
    return sorted(data, key=abs, reverse=reverse)


def sort2(data, reverse=False):
    return sorted(data, key=lambda x: abs(x), reverse=reverse)

