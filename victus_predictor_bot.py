
import telebot
from telebot import types
import random

TOKEN = '7823798112:AAF-tbAk0US9DmnVWtVy5_LHYF9IDTTopIs'
bot = telebot.TeleBot(TOKEN)

free_games = ['Over 2.5 ✅', 'GG ✅', 'Home Win ✅', '1X ✅']
vip_games = ['Sure 2+ Odds 🔥', '3+ Odds Fixed ✅', 'Correct Score 💪']

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('💪 Free Predictions', '🔥 VIP Games')
    bot.send_message(message.chat.id, f"Welcome {message.from_user.first_name}!

🏆 Victus Predictor Bot

Choose Option Below 👇", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '💪 Free Predictions')
def free(message):
    game = random.choice(free_games)
    bot.send_message(message.chat.id, f"Today's Free Game: {game}")

@bot.message_handler(func=lambda message: message.text == '🔥 VIP Games')
def vip(message):
    bot.send_message(message.chat.id, "VIP Games are only for special members.
Message Admin @YourUsername")

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.send_message(message.chat.id, "Type /start to get predictions")

print("Bot is running...")
bot.polling()
