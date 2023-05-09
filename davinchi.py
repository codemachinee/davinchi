from aiogram import Bot, executor, Dispatcher, types
# from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
from functions_file import Davinci
from paswords import *

token = lemonade

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, '''фрагмент в разработке

/help - справка по боту''')


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, '''фрагмент в разработке

/help - справка по боту''')


@dp.message_handler(content_types='text')
async def chek_message(v: types.Message):
    b = str(v.text)
    await Davinci(bot, v, b)


if __name__ == '__main__':
    executor.start_polling(dp)