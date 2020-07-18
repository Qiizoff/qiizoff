# -*- coding: utf-8 -*-
import telebot
from config import token

bot = telebot.TeleBot(token)

bot_text = '''
Привет,
Я распознаю изображения с помощью нейронных сетей!
Пришли мне фотографию, и я распознаю ее для тебя🤟
Используй /help для получения полного списка команд.
'''

bot_help = '''
Список основных команд бота:
/start
/help

Список тестовых команд бота:
/send
'''


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, bot_text)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, bot_help)


@bot.message_handler(commands=['send'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton(
        text='Отправить мою локацию', request_location=True)
    button2 = telebot.types.KeyboardButton(
        text='Отправить Мой номер', request_contact=True)
    button3 = telebot.types.KeyboardButton(
        text='Закрыть')
    markup.add(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Ваш данные:', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'D:/' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото добавлено")

    except Exception as e:
        bot.reply_to(message, e)


@bot.message_handler(content_types=["text"])
# Название функции не играет никакой роли, в принципе
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()


# ----------- Helper functions ---------------
