
def print_result(f):

    def wrapper():
        print(f.__name__)
        res = f()
        if type(res) == 'list':
            for item in res:
                print(item)
        elif type(res) == 'dict':
            for key, value in res:
                print('{} = {}'.format(key, value))
        else:
            print(res)
        return res
    return wrapper
