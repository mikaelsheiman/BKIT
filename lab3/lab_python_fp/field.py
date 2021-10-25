# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}


def field(items, *args):
    assert len(args) > 0
    rez = list()
    if len(args) == 1:
        for item in items:
            if item.keys().__contains__(args[0]):
                rez.append(item[args[0]])
    else:
        for item in items:
            d = dict()
            for key in args:
                if item.keys().__contains__(key):
                    d[key] = item[key]
            rez.append(d)
    return rez

