from enum import Enum

open_weather_token = "***"

bot_token = "***"

# Название файла базы данных
db_file = 'user_data'

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"
    STATE_CHOOSE_CITY = "STATE_CHOOSE_CITY"
    STATE_COMMON_WORK = "STATE_COMMON_WORK"
