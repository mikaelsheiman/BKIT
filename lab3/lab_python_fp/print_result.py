
def print_result(f):

    def wrapper(*args):
        print(f.__name__)
        res = f(*args)
        if isinstance(res, list):
            for item in res:
                print(item)
        elif isinstance(res, dict):
            for key in res.keys():
                print('{} = {}'.format(key, res[key]))
        else:
            print(res)
        return res
    return wrapper
