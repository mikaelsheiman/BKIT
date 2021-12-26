import telebot
import requests
import config
import dbmanager
from pprint import pprint

bot = telebot.TeleBot(config.bot_token)


def get_weather(city):
    request = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.open_weather_token}&units=metric")
    weather_data = request.json()
    pprint(weather_data)
    return weather_data


def weather_data_pars(data):
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    weather = data['weather'][0]['main']
    wind = data['wind']['speed']

    wind_description = ''
    if wind < 0.5:
        wind_description = "Ветра нет"
    elif wind < 1.7:
        wind_description = "Тихий ветер"
    elif wind < 3.3:
        wind_description = "Легкий ветер"
    elif wind < 5.4:
        wind_description = "Слабый ветер"
    elif wind < 7.9:
        wind_description = "Умеренный ветер"
    elif wind < 10.7:
        wind_description = "Свежий ветер"
    elif wind < 13.8:
        wind_description = "Сильный ветер"
    elif wind < 17.1:
        wind_description = "Крепкий ветер"
    elif wind < 20.7:
        wind_description = "Очень крепкий ветер"
    elif wind < 24.4:
        wind_description = "Шторм"
    elif wind < 28.4:
        wind_description = "Сильный шторм"
    elif wind < 32.6:
        wind_description = "Жестокий шторм"
    else:
        wind_description = "Ураган"

    recommendations = []
    if temp < 10:
        recommendations.append("Оденьтесь потеплее")
    if weather == 'Rain':
        recommendations.append("Не забудьте взять зонтик")

    weather_description = \
        (f"Погода в {data['name']} на данный момент: {weather}\n"
         f"Температура: {temp}C\n"
         f"Ощущается как {feels_like}C\n"
         f"{wind_description}\n") + str(*recommendations)

    return weather_description


start_message = "Привет! Вас приветствует бот для 5ой и 6ой лаб. На данный момент я умею показывать погоду и больше " \
                "ничего. Пожалуйста, для продолжения введите название города в котором вы живете."


@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_message(message.chat.id, start_message)
    dbmanager.set(dbmanager.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_CHOOSE_CITY.value)


@bot.message_handler(func=lambda message: dbmanager.get(
    dbmanager.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_CHOOSE_CITY.value)
def choose_city(message):
    try:
        city = message.text.lower()
        data = get_weather(city)
        dbmanager.set(dbmanager.make_key(message.chat.id, config.States.STATE_CHOOSE_CITY.value), data['name'])
        dbmanager.set(dbmanager.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_COMMON_WORK.value)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Погода', 'Ссылка на отчет', 'Сменить город')
        bot.send_message(message.chat.id, f'Выбранный город: {data["name"]}', reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, 'Возможно, вы ошиблись в написании города. Попробуйте загуглить написание '
                                          'вашего города на латинице')


@bot.message_handler(func=lambda message: dbmanager.get(
    dbmanager.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_COMMON_WORK.value,
                     content_types='text')
def common_work(message):
    if message.text.lower() == 'погода':
        data = get_weather(dbmanager.get(dbmanager.make_key(message.chat.id, config.States.STATE_CHOOSE_CITY.value)))
        description = weather_data_pars(data)
        bot.send_message(message.chat.id, description)
    elif message.text.lower() == 'ссылка на отчет' or message.text.lower() == 'ссылка на отчёт':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Лаба 5', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='Лаба 6', callback_data=6))
        markup.add(telebot.types.InlineKeyboardButton(text='ДЗ', callback_data=7))
        bot.send_message(message.chat.id, text="По какой лабораторной вы хотите увидеть отчёт?", reply_markup=markup)
    elif message.text.lower() == 'сменить город':
        dbmanager.set(dbmanager.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_CHOOSE_CITY.value)
        bot.send_message(message.chat.id, 'Введите свой город')


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    answer = ''
    if call.data == '5':
        answer = 'https://github.com/mikaelsheiman/BKIT/blob/main/%D0%9E%D1%82%D1%87%D0%B5%D1%82%20%D0%BF%D0%BE%20%D0' \
                 '%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%BE%D0%B9%20%E2%84%965.doc '
    elif call.data == '6':
        answer = 'https://github.com/mikaelsheiman/BKIT/blob/main/%D0%9E%D1%82%D1%87%D0%B5%D1%82%20%D0%BF%D0%BE%20%D0' \
                 '%BB%D0%B0%D0%B1%D0%BE%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BD%D0%BE%D0%B9%20%E2%84%966.doc '
    elif call.data == '7':
        answer = '*ссылка на ДЗ*'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


bot.polling()
