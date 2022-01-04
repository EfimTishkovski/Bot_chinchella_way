import datetime
import telebot
from telebot import types
import random

# Чтение токена из фийла
tok = open('TOKEN.txt', 'r')
TOKEN = tok.read()

bot = telebot.TeleBot(TOKEN)             # Создание экземпляра бота и подключение токена
# Источник мудрости Шинниллы
citate_mass = ['Я скала! Я кремень!',
               'Муррррр...©Кот',
               'Чужая душа - потёмки, но ингда нужно сделать этот шаг в темноту.',
               'Немогу - значит не могу, не можешь и не надо, остановись, поверни назад и останешся жив. ©Анатолий Букреев.',
               'Истории о деньгах и успехе не удивительны, история о том что кто-то по настоящему любил, по настоящему дружил, удивительна',
               'Сейчас модно, что никто никого ни ждёт и не держит, - это ошибка',
               'В тысяче слов нет смысла.',
               'Слова имеют силу.',
               'Покой для покойников',
               'пока жив, никогда не поздно',
               'Горные ветра на раз выдувают всю дурь из головы'
]
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
    markup.add(btn_source, btn_citation)                             # Добавление кнопок
    bot.reply_to(messege, 'Чтобы поговорить с шиншилой, жми на кнопки ниже', reply_markup=markup)

# Функция работы меню помощи(/help)
@bot.message_handler(commands=['help'])
def help_post(message):
    bot.send_message(message.chat.id,   '/start - Запустить бота заново\n' +
                                        '/help - Запустить меню справки\n' +
                                        'Источник - Узнать откуда всё началось\n' +
                                        'Цитата - Получить рандомную цитату из запасов шиншиллы\n' +
                                        '"Послание" - Написать в сообщении и шиншила примет и запомнит ваше послание\n')

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
            bot.send_message(message.chat.id, 'Девиз: Я скала, я кремень!')
        elif message.text == 'Цитата':
            #bot.send_message(message.chat.id, 'Тут будет цитата из списка.')
            bot.send_message(message.chat.id, random.choice(citate_mass))
        elif message.text == 'Послание':
            messege_to_chinchella(message)
        else:
            bot.send_message(message.chat.id, 'Я не монимаю слов твоих.')

#Функация обработки сообщения от пользователя
def messege_to_chinchella(message):
    msg = bot.send_message(message.chat.id, 'Я слушаю тебя.')
    bot.register_next_step_handler(msg, mess_from_walker)

def mess_from_walker(message):
    try:
        file = open('message_store.txt', 'a', encoding='utf-8')
        print('Сообщение:',message.text, file=file, end=' ')
        print('От кого:', message.from_user.first_name, file=file, end=' ')
        print('id:', message.from_user.id, file=file, end=' ')
        print('Время:', datetime.datetime.now(), file=file)
        file.close()
        bot.send_message(message.chat.id, 'Я услышала слова твои!')
    except:
        bot.send_message(message.chat.id, 'Я услышала, но не запомнила.')

bot.polling(none_stop=True, interval=0)       # Опрос сервера, не написал ли кто-нибудь?