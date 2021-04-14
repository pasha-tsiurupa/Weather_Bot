import requests
import config
import telebot

url = 'http://api.openweathermap.org/data/2.5/weather'

bot = telebot.TeleBot(config.api_telegram)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.png', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Welcome,' + str(message.from_user.username) + ',' + '\n' +
                     'Input city name!')


@bot.message_handler(content_types=['text'])
def weather_send(message):
    s_city = message.text
    try:
        params = {'APP_ID': config.api_weather,
                  'q': s_city,
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
        bot.send_message(message.chat.id, s_city + 'not found')


if __name__ == '__main__':
    bot.polling(none_stop=True)
