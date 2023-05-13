from aiogram import Bot, executor, Dispatcher
from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime
from functions_file import Davinci, statistic, platezhy
from keyboards import *
from paswords import *

#token = lemonade
token = codemashine_test

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, '''приветственный текст /help - справка по боту''')
    await buttons(bot, message).menu_buttons()


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, '''фрагмент в разработке

/help - справка по боту''')


@dp.message_handler(content_types='text')
async def chek_message(v: types.Message):
    if v.text == 'Мой статус 🤘🏻':
        answer_message = await bot.send_message(v.chat.id, f'загрузка..⏳')
        await bot.edit_message_text(await statistic().status(message=v), v.chat.id, answer_message.message_id)
    elif v.text == 'Инструкция 📋':
        await bot.send_message(v.chat.id, f'Фрагмент в разработке')
    elif v.text == 'Примеры пользования ✅':
        await bot.send_message(v.chat.id, f'Фрагмент в разработке')
    elif v.text == 'О нас ⁉️':
        await bot.send_message(v.chat.id, f'Фрагмент в разработке')
    elif v.text == 'Оформить подписку 💵':
        await buttons(bot, v).oplata_buttons(await platezhy(bot, v).url_generation())
    else:
        b = str(v.text)
        answer_message = await bot.send_message(v.chat.id, f'загрузка..⏳')
        proverka = await statistic().proverka(message=v)
        await Davinci(bot, v, b, answer_message, proverka)


@dp.callback_query_handler()
async def chek_callback(callback: types.CallbackQuery):
    if callback.data == 'Оплачено':
        await platezhy(bot, callback).chec_control()


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    #scheduler.add_job(statistic().obnulenie, "cron", day_of_week='mon-sun', hour=0)
    scheduler.add_job(statistic().obnulenie, "interval", hours=6)
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)