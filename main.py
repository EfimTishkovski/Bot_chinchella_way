import datetime
import time
import telebot
from telebot import types
import random

last_citate = ''                # Глобальная переменная для цитат

# Чтение токена из фийла
tok = open('TOKEN.txt', 'r')
TOKEN = tok.read()

bot = telebot.TeleBot(TOKEN)   # Создание экземпляра бота и подключение токена
# Источник мудрости Шиншиллы
citate_mass = ['Я скала! Я кремень!',
               'Муррррр...©Кот',
               'Чужая душа - потёмки, но ингда нужно сделать этот шаг в темноту.',
               'Немогу - значит не могу, не можешь и не надо, остановись, поверни назад, и останешся жив. ©Анатолий Букреев.',
               'Истории о деньгах и успехе не удивительны, история о том что кто-то по настоящему любил, по настоящему дружил, удивительна.',
               'Сейчас модно, что никто никого ни ждёт и не держит, - это ошибка.',
               'В тысяче слов нет смысла.',
               'Слова имеют силу.',
               'Покой - для покойников',
               'Пока жив, никогда не поздно.',
               'Горные ветра на раз выдувают всю дурь из головы.',
               'Таков путь.©Мандалорец',
               'Отступление ещё не бегство. Отход, перегрупировка и новый удар.',
               'Цой Жив!',
               'Пусть дорога трудна, но зато без оков',
               'Надежда прочна, даже крепче чем сталь',
               'Горы - это храм, там не место для понтов',
               'Порхай как бабочка, падай как шкаф.',
               'Будь твёрд и спокоек как просроченный пряник.',
               'Здравствуйте, дорогие мои радиофобы и радиофилы!©Айзон',
               'Там нас ждёт перспективная дыра!',
               'Яндекс шишига - транспорт туриста',
               'Быть собой нужно не привлекая внимание санитаров.',
               'Если вы разговариваете с вещами это не проблема, проблема - это кога они начинают отвечать',
               'Любая сила безлика, что она будет нести зависит то того кто её использует.',
               'Bella! horida bella!',
               'Лекго быть храбрым сидя на диване',
               'Иногда чудеса случаются сами, но чаще всего их приходится организовывать.',
               'Плохой человек долго над бездной не провисит.'
]
print('Запущено')

@bot.message_handler(commands=['start'])      # Создание стартового сообщения
def start_messege(messege):
    bot.send_message(messege.chat.id, 'Приветствую странник! Ты вступил на путь шиншиллы.')  # Само сообщение
    picture = open('chichella.webp', 'rb')     # Создание переменной с каратинкой
    time.sleep(0.5)  # Задержка, чтобы сообщения не летели как из пулемёта
    bot.send_sticker(messege.chat.id, picture) # показать картинку
    # Клавиатура (кнопки)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_source = types.KeyboardButton('Источник')                    # Создание кнопки
    btn_citation = types.KeyboardButton('Цитата')                    # Создание кнопки
    btn_message = types.KeyboardButton('Послание')                   # Создание кнопки
    markup.add(btn_source, btn_citation, btn_message)                # Добавление кнопок
    bot.reply_to(messege, 'Чтобы поговорить с шиншиллой, жми на кнопки ниже', reply_markup=markup)

# Функция работы меню помощи(/help)
@bot.message_handler(commands=['help'])
def help_post(message):
    bot.send_message(message.chat.id,   '/start - Запустить бота заново.\n' +
                                        '/help - Запустить меню справки.\n' +
                                        'Источник - Узнать откуда всё началось.\n' +
                                        'Цитата - Получить случайную цитату из запасов шиншиллы.\n' +
                                        'Послание - Шиншилла примет и запомнит ваше послание.\n' +
                                        'Шиншилла знает кое-что о людях и клубах, напишите имя и если она знает, то ответит. \n')

# Функция обработки нажатий на кнопки
@bot.message_handler(func=lambda message: True)
def menu(message):
    # проверка типа сообщения(чата) может быть private’, ‘group’, ‘supergroup’ or ‘channel’ из документации
    if message.chat.type == 'private':
        # Обработчик кнопки источник
        if message.text == 'Источник':
            source_photo = open('source.jpg', 'rb')
            bot.send_photo(message.chat.id, source_photo)
            time.sleep(0.5) # Задержка, чтобы сообщения не летели как из пулемёта
            bot.send_message(message.chat.id, 'Этот мем стал началом пути шиншиллы.')
            time.sleep(0.5)
            bot.send_message(message.chat.id, 'Вначале, это был путь страданий, но потом он стал путём силы.')
            time.sleep(0.5)
            bot.send_message(message.chat.id, 'Девиз: Я скала, я кремень!')
        elif message.text == 'Цитата':
            # Небольшая фича чтобы небыло одинаковых цитат друг за другом
            global last_citate
            while True:
                new_citate = random.choice(citate_mass)
                if new_citate != last_citate:
                    # Если цитата не такая как предыдущая, выводим её
                    bot.send_message(message.chat.id, new_citate)
                    last_citate = new_citate
                    break            # Выход из цикла, иначе зациклимся)
        elif message.text.lower() == 'послание':
            messege_to_chinchella(message)
        # Пасхалки =)
        elif message.text.lower() == 'кот':
            audio = open('meow-and-purr.mp3', 'rb')
            bot.send_message(message.chat.id, 'Муррррр =)')
            time.sleep(0.5)
            bot.send_audio(message.chat.id, audio, title='Мууррчание')
            audio.close()
        elif message.text.lower() == 'артур':
            bot.send_message(message.chat.id, 'Здарова камрад!')
        elif message.text.lower() == 'геликтит':
            bot.send_message(message.chat.id, 'Пещеры ждут! Арабика скучает)')
        elif message.text.lower() == 'ближайший поход':
            bot.send_message(message.chat.id, 'Ееее! Гнездо душевного туризма))')
        elif message.text.lower() == 'альтаир':
            bot.send_message(message.chat.id, 'Братья по разуму)')
        elif message.text.lower() == 'лида':
            bot.send_message(message.chat.id, 'Надежда и опора руковода, страшна в гневе))')
        elif message.text.lower() == 'виталик':
            bot.send_message(message.chat.id, 'Просто хороший парень и до кучи комендант')
        elif message.text.lower() == 'наташа':
            bot.send_message(message.chat.id, 'На словах страшна, добрая внутри =)')
        elif message.text.lower() == 'андрей':
            bot.send_message(message.chat.id, 'Слава завснару! =)')
        elif message.text.lower() == 'отправить хранилище':
            bot.send_message(message.chat.id, 'Отправила')
            file_storage = open('message_store.txt', 'r', encoding='utf-8')
            bot.send_document(message.chat.id, file_storage)
            file_storage.close()
        else:
            bot.send_message(message.chat.id, 'Я не монимаю слов твоих.')

#Функция обработки сообщения от пользователя
def messege_to_chinchella(message):
    msg = bot.send_message(message.chat.id, 'Я слушаю тебя.')
    bot.register_next_step_handler(msg, mess_from_walker)
# Функция сохранения посланий от пользователей
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

#bot.polling(none_stop=True, interval=0)       # Опрос сервера, не написал ли кто-нибудь?

# Дополнение чтобы бот при падении перезапускался
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)  # Опрос сервера, не написал ли кто-нибудь?
        except Exception as ex:
            time.sleep(3)
            print(ex)