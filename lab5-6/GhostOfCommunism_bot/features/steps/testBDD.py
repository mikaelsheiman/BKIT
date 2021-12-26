from behave import given, when, then
from bot import get_weather, weather_data_pars
from test_cases import test_case, expected


@given('Я живу в городе {city}')
def step_impl(context, city: str):
    context.city = str(city)


@when('Я отправляю запрос к openweather')
def step_impl(context):
    context.res = get_weather(context.city)


@then('Я должен получить файл')
def step_impl(context):
    assert context.res['name'].lower() == context.city.lower()


@given('У меня есть данные')
def step_impl(context):
    context.data = test_case


@when('Я преобразую их в текст сообщения')
def step_impl(context):
    context.res = weather_data_pars(context.data)


@then('Я должен получить ожидаемый текст')
def step_impl(context):
    assert context.res == expected
