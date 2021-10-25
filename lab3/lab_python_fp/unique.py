# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, ignore_case=False):
        self.items = list(items)
        self.ignore_case = ignore_case

    def __next__(self):
        if len(self.items) == 0:
            raise StopIteration
        rez = self.items[0]
        if self.ignore_case:
            self.items = list(filter(lambda x: str(x).lower() != str.lower(rez), self.items))
        else:
            self.items = list(filter(lambda x: x != rez, self.items))
        return rez

    def __iter__(self):
        return self
