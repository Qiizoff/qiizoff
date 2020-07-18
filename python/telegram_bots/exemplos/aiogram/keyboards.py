from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)

greet_kb2 = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)


# markup_request = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(KeyboardButton('Отправить свой контакт ☎️', request_contact=True)).add(KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
markup_request = ReplyKeyboardMarkup(
    one_time_keyboard=True, resize_keyboard=True)
sendtel = KeyboardButton('Отправить телефон ☎️', request_contact=True)
sendloc = KeyboardButton('Отправить геопозицию 🗺️', request_location=True)
sendclose = ('Закрыть')
markup_request.add(sendtel, sendloc)
markup_request.row(sendclose)


markup_big = ReplyKeyboardMarkup()

markup_big.add(
    button1, button2, button3, button4, button5, button6
)
markup_big.row(
    button1, button2, button3, button4, button5, button6
)

markup_big.row(button4, button2)
markup_big.add(button3, button2)
markup_big.insert(button1)
markup_big.insert(button6)
markup_big.insert(KeyboardButton('9️⃣'))

inline_btn_1 = InlineKeyboardButton(
    '/start - информация о боте', callback_data='button_start')
inline_btn_2 = InlineKeyboardButton(
    '/help - reply help menu', callback_data='button_help')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)

inline_kb_full = InlineKeyboardMarkup(row_width=2)
inline_kb_full.add(inline_btn_1).row(inline_btn_2)
inline_kb_full.add(InlineKeyboardButton('кнопка 2', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('кнопка 3', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('кнопка 4', callback_data='btn4')
inline_btn_5 = InlineKeyboardButton('кнопка 5', callback_data='btn5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton("query=''", switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton(
    "query='qwerty'", switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton(
    "Inline в этом же чате", switch_inline_query_current_chat='wasd'))
