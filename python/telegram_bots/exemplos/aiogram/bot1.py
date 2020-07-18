from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import token
import keyboards as kb


bot = Bot(token=token)
dp = Dispatcher(bot)


##


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(
            callback_query.id,
            text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉',
            show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


##


@dp.message_handler(commands=['hi1'])
async def process_hi1_command(message: types.Message):
    await message.reply("Первое - изменяем размер клавиатуры",
                        reply_markup=kb.greet_kb1)


@dp.message_handler(commands=['hi2'])
async def process_hi2_command(message: types.Message):
    await message.reply("Второе - прячем клавиатуру после одного нажатия",
                        reply_markup=kb.greet_kb2)


@dp.message_handler(commands=['hi3'])
async def process_hi3_command(message: types.Message):
    await message.reply("Третье - добавляем больше кнопок",
                        reply_markup=kb.markup3)


@dp.message_handler(commands=['hi4'])
async def process_hi4_command(message: types.Message):
    await message.reply("Четвертое - расставляем кнопки в ряд",
                        reply_markup=kb.markup4)


@dp.message_handler(commands=['hi5'])
async def process_hi5_command(message: types.Message):
    await message.reply("Пятое - добавляем ряды кнопок",
                        reply_markup=kb.markup5)


@dp.message_handler(commands=['hi7'])
async def process_hi7_command(message: types.Message):
    await message.reply("Седьмое - все методы вместе",
                        reply_markup=kb.markup_big)


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply("Убираем шаблоны сообщений",
                        reply_markup=kb.ReplyKeyboardRemove())

##


help_message = text(
    "Это урок по клавиатурам.",
    "Доступные команды:\n",
    "/start - приветствие",
    "\nШаблоны клавиатур:",
    "/hi1 - авто размер",
    "/hi2 - скрыть после нажатия",
    "/hi3 - больше кнопок",
    "/hi4 - кнопки в ряд",
    "/hi5 - больше рядов",
    "/hi6 - запрос локации и номера телефона",
    "/hi7 - все методы"
    "/rm - убрать шаблоны",
    "\nИнлайн клавиатуры:",
    "/1 - первая кнопка",
    "/2 - сразу много кнопок",
    sep="\n"
)

bot_start = '''
Привет,
Я распознаю изображения с помощью нейронных сетей!
Пришли мне фотографию, и я распознаю ее для тебя🤟

Используй комманду /help для получения полного списка команд.
'''

bot_help = text(
    "Список основных команд бота:",
    "/start - информация о боте",
    "/help - reply меню",
    "\nСписок тестовых команд бота:",
    "/send - отправить телефон/геопозицию",
    "/inline - inline меню",
    "/other - прочее inline меню",
    sep="\n"
)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.chat.id, bot_start)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await bot.send_message(message.chat.id, bot_help)


@dp.message_handler(commands=['send'])
async def process_hi6_command(message: types.Message):
    await bot.send_message(message.chat.id, "Отправить личные данные:", reply_markup=kb.markup_request)


@dp.message_handler(commands=['inline'])
async def process_command_1(message: types.Message):
    await bot.send_message(message.chat.id, "Список inline команд бота:", reply_markup=kb.inline_kb1)


@dp.message_handler(commands=['other'])
async def process_command_2(message: types.Message):
    await bot.send_message(message.chat.id, "Прочие inline команды бота:", reply_markup=kb.inline_kb_full)


@dp.callback_query_handler(lambda c: c.data == 'button_start')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
    await bot.send_message(callback_query.from_user.id, bot_start)
    # await bot.send_message(message.chat.id, bot_start)


@dp.callback_query_handler(lambda c: c.data == 'button_help')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, bot_help)

if __name__ == '__main__':
    executor.start_polling(dp)
