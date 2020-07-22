from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

reply = ReplyKeyboardMarkup(resize_keyboard=True)
reply1 = KeyboardButton('/start')
reply2 = KeyboardButton('/help')
reply3 = KeyboardButton('/send')
reply4 = KeyboardButton('/'+'inline')
reply.row(reply1, reply2, reply3).add(reply4)

send = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
send1 = KeyboardButton('Отправить номер ☎️', request_contact=True)
send2 = KeyboardButton('Отправить геопозицию 🗺️', request_location=True)
send3 = ('Закрыть')
send.add(send1, send2)
send.row(send3)

inline = InlineKeyboardMarkup()
inline1 = InlineKeyboardButton('start', callback_data='button_start')
inline2 = InlineKeyboardButton('help', callback_data='button_help')
inline3 = InlineKeyboardButton('reply', callback_data='button_reply')
inline.row(inline1, inline2).add(inline3)


inline_full = InlineKeyboardMarkup(row_width=2)
inline_full.add(inline1).row(inline2)

# inline_kb_full.add(InlineKeyboardButton('кнопка 2', callback_data='btn2'))
# inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
# inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
# inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
# inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
# inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
# inline_kb_full.insert(InlineKeyboardButton(
#     "query='qwerty'", switch_inline_query='qwerty'))
# inline_kb_full.insert(InlineKeyboardButton(
#     "Inline в этом же чате", switch_inline_query_current_chat='wasd'))
