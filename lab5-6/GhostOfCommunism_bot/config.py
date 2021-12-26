from enum import Enum

open_weather_token = "33e997c592e4784aa35564edebfb6be2"

bot_token = "5040933736:AAFyBdBDDBijbVTNY0OePVXgCT5YoWubumY"

db_file = 'user_data'

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_CHOOSE_CITY = "STATE_CHOOSE_CITY"
    STATE_COMMON_WORK = "STATE_COMMON_WORK"
