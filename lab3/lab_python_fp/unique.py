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
            for i in self.items.copy(): #Почему здесь без копии не работает
                if str.lower(i) == str.lower(rez):
                    print('x', i)
                    self.items.remove(i)
        else:
            while rez in self.items: #А здесь работает?
                self.items.remove(rez)
        return rez

    def __iter__(self):
        return self
