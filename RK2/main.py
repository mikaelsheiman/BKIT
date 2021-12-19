from operator import itemgetter


class PL:
    def __init__(self, pl_id, name):
        self.pl_id = pl_id
        self.name = name


class Syntax:
    def __init__(self, syn_id, name, pl_id, usefulness_grade=1.0):
        self.syn_id = syn_id
        self.name = name
        self.pl_id = pl_id
        self.usefulness_grade = usefulness_grade


class PL_Syn:
    def __init__(self, pl_id, syn_id):
        self.pl_id = pl_id
        self.syn_id = syn_id


def request1(PLs, Syntaxes):
    one_to_many = [(syn.name, pl.name)
                   for pl in PLs
                   for syn in Syntaxes
                   if (pl.pl_id == syn.pl_id)]
    result = sorted(one_to_many, key=itemgetter(1))
    return result
    #print(*result, sep="\n")


def request2(PLs, Syntaxes):
    one_to_many = [(syn.name, syn.usefulness_grade, pl.name)
                   for pl in PLs
                   for syn in Syntaxes
                   if (pl.pl_id == syn.pl_id)]
    result = list()
    for pl in PLs:
        syns = list(filter(lambda i: i[2] == pl.name, one_to_many))
        if len(syns) != 0:
            sum_ug = sum(ug for _, ug, _ in syns)
            result.append((pl.name, sum_ug))
    result = sorted(result, key=itemgetter(1), reverse=True)
    return result
    #print(*result, sep="\n")


def request3(PLs, Syntaxes, PL_Syns):
    many_to_many_temp = [(pl.name, p_s.syn_id)
                         for pl in PLs
                         for p_s in PL_Syns
                         if p_s.pl_id == pl.pl_id]
    many_to_many = [(pl_name, syn.name)
                    for pl_name, syn_id in many_to_many_temp
                    for syn in Syntaxes
                    if syn.syn_id == syn_id]

    result = dict()
    for pl in PLs:
        if "C" in pl.name:
            filtered = list(filter(lambda i: i[0] == pl.name, many_to_many))
            s_names = [i for _, i in filtered]
            result[pl.name] = s_names
    return result
    #print(result)


def main():
    pass

