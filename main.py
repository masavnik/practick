import telebot
from config import token, profession
from time import sleep

bot = telebot.TeleBot(token)

name = ''
age = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Приветствую тебя друг")
    bot.send_message(message.from_user.id, 'Для начала как тебя зовут?')


@bot.message_handler(content_types=['text'])
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, f'Отлично {name}, сколько вам лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except SyntaxError:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')

    bot.send_message(message.from_user.id, f'Тебе {str(age)} лет, тебя зовут {name}?\n'
                                           f'Напиши: да или нет')
    bot.register_next_step_handler(message, answer)


def answer(message):
    if message.text == 'да':
        bot.send_message(message.from_user.id, f'Олично, тогда продлжаем\n'
                                               f'Загружаем профессии...')
        sleep(2)
        bot.send_message(message.from_user.id, f'{name}, Профессии загрузились')
        for i_prof, y_prof in enumerate(profession):
            sleep(1)
            bot.send_message(message.from_user.id, f'{i_prof + 1} - {y_prof}')
        bot.send_message(message.from_user.id, f'{name}, Выберете цыфру')
    bot.register_next_step_handler(message, profession_get)


def profession_get(message):
    if message.text == '1':
        with open('svar.txt', 'r', encoding='utf-8') as file:
            bot.send_message(message.from_user.id, file.read())
    if message.text == '2':
        with open('sles.txt', 'r', encoding='utf-8') as file:
            bot.send_message(message.from_user.id, file.read())
    if message.text == '3':
        with open('teh.txt', 'r', encoding='utf-8') as file:
            bot.send_message(message.from_user.id, file.read())
    if message.text == '4':
        with open('manager.txt', 'r', encoding='utf-8') as file:
            bot.send_message(message.from_user.id, file.read())


if __name__ == '__main__':
    bot.infinity_polling()
