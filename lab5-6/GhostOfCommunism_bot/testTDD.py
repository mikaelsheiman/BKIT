import unittest
import bot
from test_cases import test_case, expected


class BotTest(unittest.TestCase):
    def test_get_request(self):
        result = bot.get_weather("moscow")
        self.assertEqual("moscow", result['name'].lower())

    def test_weather_data_pars(self):
        result = bot.weather_data_pars(test_case)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
