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
    btn_message_to_source = types.KeyboardButton('Послание Шиншилле') # Создание кнопки
    markup.add(btn_source, btn_citation, btn_message_to_source)      # Добавление кнопок
    bot.reply_to(messege, 'Чтобы поговорить с шиншилой, жми на кнопки ниже', reply_markup=markup)

# Функция обработки нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def menu(message):
    # проверка типа сообщения(чата) может быть private’, ‘group’, ‘supergroup’ or ‘channel’ из документации
    if message.chat.type == 'private':
        # Обработчик кнопки источник
        if message.text == 'Источник':
            source_photo = open('source.jpg', 'rb')
            bot.send_photo(message.chat.id, source_photo)
            bot.send_message(message.chat.id, 'Этот мем стал началом пути шиншиллы.')
            bot.send_message(message.chat.id, 'Вначале, это был путь страданий, но потом он стал путём силы.')
            bot.send_message(message.chat.id, 'Девиз: Я скала, я кремень!.')
        elif message.text == 'Цитата':
            bot.send_message(message.chat.id, 'Тут будет цитата из списка.')
        elif message.text == 'Послание Шиншилле':
            bot.send_message(message.chat.id, 'Неопределённа кнопка, может не понадобится.')
        elif message.text == 'Послание':
            messege_to_chinchella(message)
        else:
            bot.send_message(message.chat.id, 'Я не монимаю слов твоих.')

#Функация обработки сообщения от пользователя
def messege_to_chinchella(message):
    msg = bot.send_message(message.chat.id, 'Я слушаю тебя.')
    bot.register_next_step_handler(msg, mess_from_walker)

def mess_from_walker(message):
    print(message.text)
    #print(message.from_user)
    print('От кого:')
    print(message.from_user.first_name)
    print(message.date)
    #walker = []
    #walker.append(message.text)
    bot.send_message(message.chat.id, 'Я услышала слова твои!')


bot.polling(none_stop=True, interval=0)       # Опрос сервера, не написал ли кто-нибудь?
