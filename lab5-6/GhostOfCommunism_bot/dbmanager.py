from vedis import Vedis
import config


def get(key):
    with Vedis(config.db_file) as db:
        try:
            return db[key].decode()
        except KeyError:
            return config.States.STATE_START.value


def set(key, value):
    with Vedis(config.db_file) as db:
        try:
            db[key] = value
            return True
        except:
            print("!!!!!!!!!!!Проблема!!!!!!!!!!!")
            return False


def make_key(chatid, keyid):
    res = str(chatid) + '__' + str(keyid)
    return res
