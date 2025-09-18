from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from Weather import Weather
from temp_gpaph import plot_temperature
import datetime
import os

TOKEN = "7975396025:AAGg2DC2sYvMOEYUpRDtS87EFJUFwh67OWA"
LOCATIONS = {"Moscow":"Moscow","Pskov":"Pskov","Udomlya":"Udomlya"}

bot = TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=3)
    for name in LOCATIONS.keys():
        item_button = KeyboardButton(name)
        markup.add(item_button)
    bot.send_message(message.chat.id, "Select the location, when you want to know weather ", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text in LOCATIONS.keys())
def send_temp(message):
    photo_path = './images/my_temperature_plot.png'
    my_weather = Weather(location=message.text, date=str(datetime.date.today()))
    plot_temperature(my_weather.get_temperature_hours(), message.text, photo_path)

    try:
        if not os.path.exists(photo_path):
            bot.send_message(message.chat.id, "Location not exists!")
            return
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=f"Here`s the temperature in {message.text} today.")
    except Exception as e:
        bot.send_message(message.chat.id, "Location not exists!")

bot.infinity_polling()
