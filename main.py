import requests
import config
import telebot

url = 'http://api.openweathermap.org/data/2.5/weather'

bot = telebot.TeleBot(config.api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Welcome, ' + str(message.from_user.first_name) + ',' + '\n' + 'Input city name!')


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     '/start запуск бота\n/help команды бота\nчтоб узнать погоду напишите в чат название города')


@bot.message_handler(content_types=['text'])
def test(message):
    city_name = message.text

    try:
        params = {'APPID': config.api_weather,
                  'q': city_name,
                  'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()

        bot.send_message(message.chat.id, 'In the city of' + str(
            weather['name'] + 'temperature' + str(float(weather['main']['temp'])) + ' &#8451;' + 'C' + '\n' +
            'Max temperature' + str(float(weather['main']['temp_max'])) + ' &#8451;' + 'C' + '\n' +
            'Min temperature' + str(float(weather['main']['temp_min'])) + ' &#8451;' + 'C' + '\n' +
            'Wind' + str(float(weather['main']['speed'])) + '\n' +
            'Pressure' + str(float(weather['main']['pressure'])) + '\n' +
            'Humidity' + str(float(weather['main']['humidity'])) + '\n'))

    except:
        bot.send_message(message.chat.id, 'City' + city_name + ' not found')


if __name__ == '__main__':
    bot.polling(none_stop=True)
