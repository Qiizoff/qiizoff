from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.dispatcher import Dispatcher

from config import token
import keyboards as kb


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        # await bot.answer_callback_query(callback_query.id, text='Нажата вторая кнопка')
        # await bot.send_message(message.chat.id, "Прочие inline команды бота:", reply_markup=kb.inline_kb_full)
        await bot.send_message(message.chat.id, "Отправить личные данные:", reply_markup=kb.inline_request)
    elif code == 5:
        await bot.answer_callback_query(callback_query.id, text='Нажата кнопка с номером 5.\nА этот текст может быть длиной до 200 символов 😉', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата инлайн кнопка! code={code}')


bot_start = '''
Привет,
Я распознаю изображения с помощью нейронных сетей!
Пришли мне фотографию, и я распознаю ее для тебя🤟

Используй комманду /help для получения полного списка команд.
'''

bot_help = text(
    "Список основных команд бота:",
    "/start - информация о боте",
    "/help - команды бота",
    "\nСписок тестовых команд бота:",
    "/send - отправить телефон/геопозицию",
    "/inline - inline меню",
    "/reply - reply меню",
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
async def process_send_command(message: types.Message):
    await bot.send_message(message.chat.id, "Отправить личные данные:", reply_markup=kb.send)


@dp.message_handler(commands=['inline'])
async def process_inline_command(message: types.Message):
    await bot.send_message(message.chat.id, "Список основных inline команд бота:", reply_markup=kb.inline)


@dp.message_handler(commands=['reply'])
async def process_reply_command(message: types.Message):
    await bot.send_message(message.chat.id, "Список основных reply команд бота:", reply_markup=kb.reply)


@dp.message_handler(commands=['other'])
async def process_other_command(message: types.Message):
    await bot.send_message(message.chat.id, "Прочие inline команды бота:", reply_markup=kb.inline_full)


@dp.callback_query_handler(lambda c: c.data == 'button_start')
async def process_button_start(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, bot_start)
    # await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')
    # await bot.send_message(message.chat.id, bot_start)


@dp.callback_query_handler(lambda c: c.data == 'button_help')
async def process_button_help(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, bot_help)


@dp.callback_query_handler(lambda c: c.data == 'button_reply')
async def process_button_reply(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '/reply')


if __name__ == '__main__':
    executor.start_polling(dp)
