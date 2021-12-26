Feature: wheather

  Scenario Outline: get_request
    Given Я живу в городе <city>
    When Я отправляю запрос к openweather
    Then Я должен получить файл

    Examples: Cities
    |city|
    |moscow|
    |perm  |
    |berlin|
    |omsk  |

  Scenario: weather_data_pars
    Given У меня есть данные
    When Я преобразую их в текст сообщения
    Then Я должен получить ожидаемый текст