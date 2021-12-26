import unittest
import bot


class BotTest(unittest.TestCase):
    def test_get_request(self):
        result = bot.get_weather("moscow")
        self.assertEqual(True, result is not None)  # add assertion here

    def test_weather_data_pars(self):
        result = bot.weather_data_pars(test_case)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

expected = \
    (f"Погода в Москве на данный момент:\n"
     f"Температура: -6.21C\n"
     f"Ощущается как -13.21C\n"
     f"Умеренный ветер")
test_case = {'base': 'stations',
             'clouds': {'all': 100},
             'cod': 200,
             'coord': {'lat': 55.7522, 'lon': 37.6156},
             'dt': 1640526500,
             'id': 524901,
             'main': {'feels_like': -13.21,
                      'grnd_level': 978,
                      'humidity': 86,
                      'pressure': 997,
                      'sea_level': 997,
                      'temp': -6.21,
                      'temp_max': -5.76,
                      'temp_min': -7.14},
             'name': 'Moscow',
             'snow': {'1h': 0.22},
             'sys': {'country': 'RU',
                     'id': 2018597,
                     'sunrise': 1640498360,
                     'sunset': 1640523640,
                     'type': 2},
             'timezone': 10800,
             'visibility': 511,
             'weather': [{'description': 'light snow',
                          'icon': '13n',
                          'id': 600,
                          'main': 'Snow'}],
             'wind': {'deg': 219, 'gust': 16.38, 'speed': 7.43}}
