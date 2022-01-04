import telebot
from telebot import types
import random
#import xlrd

# Чтение токена из фийла
tok = open('TOKEN.txt', 'r')
TOKEN = tok.read()

bot = telebot.TeleBot(TOKEN)             # Создание экземпляра бота и подключение токена

print('Запущено')

@bot.message_handler(commands=['start'])      # Создание стартового сообщения
def start_messege(messege):
    bot.send_message(messege.chat.id, 'Приветствую странник! Ты вступил на путь шиншиллы.')  # Само сообщение
    picture = open('chichella.webp', 'rb')     # Создание переменной с каратинкой
    bot.send_sticker(messege.chat.id, picture) # показать картинку

    # Клавиатура (кнопки)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_source = types.KeyboardButton('Источник')                    # Создание кнопки
    btn_citation = types.KeyboardButton('Цитата')                    # Создание кнопки
    btn_message_to_source = types.KeyboardButton('Послание Шиншиле') # Создание кнопки
    markup.add(btn_source, btn_citation, btn_message_to_source)      # Добавление кнопок
    bot.reply_to(messege, 'Чтобы поговорить с шиншилой, жми на кнопки ниже', reply_markup=markup)

bot.polling(none_stop=True, interval=0)       # Опрос сервера, не написал ли кто-нибудь?
