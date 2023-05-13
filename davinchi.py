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
    await bot.send_message(message.chat.id,  f'Чатбот умеет:\n\n'
                                          f'1. Писать и редактировать текст\n'
                                          f'2. Переводить с любого языка на любой\n'
                                          f'3. Писать и редактировать код\n'
                                          f'4. Отвечать на вопросы\n'
                                          f'5. Писать посты/описание к товарам\n\n '
                                             f'Чтобы воспользоваться ботом просто напишите запрос в чат\n\n'
                                             f'/help - справка по боту'
                           )
    await buttons(bot, message).menu_buttons()


@dp.message_handler(commands=['help'])
async def command_start(message: types.Message):
    await bot.send_message(message.chat.id, f'Бесплатно доступно 3 запроса в день\n'
                                            f'Безлимитное количество запросов:\n'
                                            f'сутки - 100 руб.\n'
                                            f'неделя - 500 руб.')


@dp.message_handler(content_types='text')
async def chek_message(v: types.Message):
    if v.text == 'Мой статус 🤘🏻':
        answer_message = await bot.send_message(v.chat.id, f'загрузка..⏳')
        await bot.edit_message_text(await statistic().status(message=v), v.chat.id, answer_message.message_id)
    elif v.text == 'Инструкция 📋':
        await bot.send_message(v.chat.id, f'Чатбот умеет:\n\n'
                                          f'1. Писать и редактировать текст\n'
                                          f'2. Переводить с любого языка на любой\n'
                                          f'3. Писать и редактировать код\n'
                                          f'4. Отвечать на вопросы\n'
                                          f'5. Писать посты/описание к товарам\n\n'
                                          f'Вы можете общаться с ботом, как с живым собеседником, задавая вопросы на '
                                          f'любом языке. Обратите внимание, '
                                          f'что иногда нейросеть придумывает факты, а также обладает ограниченными '
                                          f'знаниями о событиях после 2021 года. Учтите, что нейросеть обучена на '
                                          f'английском языке, старайтесь использовать простые формулировки чтобы '
                                          f'исключить неверное толкование при переводе.\n\n'
                                          f'✉️ Чтобы получить текстовый ответ, просто напишите в чат ваш вопрос.\n'
                                          f'При ответе на запрос бот выдает '
                                          f'ограниченное количество информации, чтобы увеличить выдачу просто напишите '
                                          f'боту: "продолжить".')
    elif v.text == 'Примеры пользования ✅':
        await bot.send_photo(v.chat.id, types.InputFile('1.png'), 'Пример сочинения ЭССЭ')
        await bot.send_photo(v.chat.id, types.InputFile('2.png'), 'Пример с запросом теоремы Баеса')
        await bot.send_photo(v.chat.id, types.InputFile('3.png'), 'Пример с переводом')
        await bot.send_photo(v.chat.id, types.InputFile('4.png'), 'Пример составления структуры диплома')
        await bot.send_photo(v.chat.id, types.InputFile('5.png'), 'Пример составления введения к диплому')
    elif v.text == 'О нас ⁉️':
        await bot.send_message(v.chat.id, f'Вопросы и предложения по работе бота: @hlapps')
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