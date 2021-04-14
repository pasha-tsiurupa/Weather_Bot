import requests
import telebot
import config

url = 'http://api.openweathermap.org/data/2.5/weather'

bot = telebot.TeleBot(config.api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Welcome, ' + str(message.from_user.first_name) + '!' + '\n' + 'Input city name')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id, 'To find out the weather, write the name of the city in the chat')


@bot.message_handler(content_types=['text'])
def test(message):
    city_name = message.text

    try:
        params = {
            'APPID': config.api_weather,
            'q': city_name,
            'units': 'metric'
        }
        result = requests.get(url, params=params)
        weather = result.json()

        bot.send_message(message.chat.id, 'In ' + str(weather['name']) + '\n' +
                         'Temperature:  ' + str(int(weather['main']['temp'])) + '\xb0C' + '\n' +
                         'Max temperature:  ' + str(int(weather['main']['temp_max'])) + '\xb0C' + '\n' +
                         'Min temperature:  ' + str(int(weather['main']['temp_min'])) + '\xb0C' + '\n' +
                         'Wind:  ' + str(int(weather['wind']['speed'])) + ' m/s' + '\n' +
                         'Pressure:  ' + str(int(weather['main']['pressure'])) + ' hpa' + '\n' +
                         'Humidity:  ' + str(int(weather['main']['humidity'])) + '%' + '\n'
                         )

    except:
        bot.send_message(message.chat.id, 'City ' + city_name + ' not found')


if __name__ == '__main__':
    bot.polling(none_stop=True)
