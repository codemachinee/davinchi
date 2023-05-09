from aiogram import Bot, executor, Dispatcher, types
from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
from functions_file import Davinci, statistic
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
    answer_message = await bot.send_message(v.chat.id, f'загрузка..')
    proverka = await statistic().proverka(message=v)
    await Davinci(bot, v, b, answer_message, proverka)


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(statistic().obnulenie(), "cron", day_of_week='mon-sun', hour=0)
    scheduler.start()
    executor.start_polling(dp)