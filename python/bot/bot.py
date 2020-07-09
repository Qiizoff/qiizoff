# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

bot_text = '''
Bip-bop human,

I classify images using neural networks 🚀

Send me pictures, and I will classify them for you 🤟

Created with ❤️ by Alain Perkaz. @wh_image_classificator_bot
Source code on https://glitch.com/~telegram-image-classfication-bot
'''

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')


# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(
#         message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, bot_text)

# @bot.message_handler(content_types=['photo'])
# def handle_docs_photo(message):

#     try:

#         file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
#         downloaded_file = bot.download_file(file_info.file_path)

#         src = '/files/'+file_info.file_path
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
#         bot.reply_to(message, "Фото добавлено")

#     except Exception as e:
#         bot.reply_to(message, e)


@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):

    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = 'D:/GitHub//qiizoff.github.io//python//bot//files//' + file_info.file_path
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото добавлено")

    except Exception as e:
        bot.reply_to(message, e)


@ bot.message_handler(content_types=["text"])
# Название функции не играет никакой роли, в принципе
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()


# ----------- Helper functions ---------------
