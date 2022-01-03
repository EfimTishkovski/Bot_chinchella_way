import telebot
from telebot import types
import random
import xlrd

bot = telebot.TeleBot('token')

@bot.message_handlers(commands=['start'])
def start_messege(messege):
    bot.send_message(messege.chat.id, 'Приветствую странник! Ты вступил на путь шиншиллы.')


bot.polling(none_stop=True, interval=0)
