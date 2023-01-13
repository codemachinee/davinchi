# -*- coding: utf-8 -*-
import telebot
import gspread
import os
from telebot import types
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from random import *
from functions_file import value_plus_one, pstat, obnulenie_stat, ball_of_fate, Davinci
from paswords import *

token = lemonade

bot = telebot.TeleBot(token)

kb1 = types.InlineKeyboardMarkup(row_width=1)
but1 = types.InlineKeyboardButton(text='Купить билет в Орёл',
                                  url='https://жд-билеты.сайт/kupit-zhd-bilety/#/moskva/orel?')
but2 = types.InlineKeyboardButton(text='Бронь стола на Привале', url='http://onmap.uz/tel/74862484006')
but3 = types.InlineKeyboardButton(text='Бронь стола 7 пятниц', url='http://onmap.uz/tel/74862490008')
but4 = types.InlineKeyboardButton(text='Бронь стола Шаривари', url='http://onmap.uz/tel/74862445303')
but5 = types.InlineKeyboardButton(text='Таблица расходов', url='https://docs.google.com/spreadsheets/d'
                                                               '/1OJVOVnfRygWLN_OIK3w7FuAh37z0eAio0AkTbF7nBf4/edit'
                                                               '#gid=431148771')
but6 = types.InlineKeyboardButton(text='Яндекс.Диск', url='https://disk.yandex.ru/client/disk/бот%20суетологов/суетологи')
but7 = types.InlineKeyboardButton(text='Важное про Орёл', callback_data='btn')
but8 = types.InlineKeyboardButton(text='Шар судьбы', callback_data='bof')
kb1.add(but1, but2, but3, but4, but5, but6, but7, but8)


def pidr():
    obnulenie_stat()
    x = choice([1, 2, 3, 4, 5, 6, 7])
    if x == 1:
        file1 = open("Я.png", 'rb')
        y = ("Игорь", file1)
        value_plus_one('A2')
        bot.send_photo('group_id', y[1])
        bot.send_message(group_id, f'''Всем привет!!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 2:
        file1 = open("Филч.png", 'rb')
        y = ("Филч", file1)
        value_plus_one('A1')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 3:
        file1 = open("Серега.png", 'rb')
        y = ("Серега", file1)
        value_plus_one('A3')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 4:
        file1 = open("Леха.png", 'rb')
        y = ("Леха(Саня)", file1)
        value_plus_one('A5')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 5:
        file1 = open("фитиль.jpg", 'rb')
        y = ("Леха(Фитиль)", file1)
        value_plus_one('A6')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 6:
        file1 = open("маугли.png", 'rb')
        y = ("Маугли", file1)
        value_plus_one('A7')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()

    if x == 7:
        file1 = open("саня.png", 'rb')
        y = ("Саня", file1)
        value_plus_one('A4')
        bot.send_photo(group_id, y[1])
        bot.send_message(group_id, f'''Всем привет!! Пидарасом дня 
{datetime.now().day}.{datetime.now().month}.{datetime.now().year} объявляется {y[0]} 
Справка по боту: /help''')
        dr()
        
        
def dr():
    if datetime.now().day == 20 and datetime.now().month == 4:
        bot.send_message(group_id, (f' Кстати, ебать сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Игорь, да именно он вне всяких рейтингов и чартов, ведь у него '
                                          f'самый большой член в этом сообществе и самый скромный нрав. Игорян с днем '
                                          f'рождения!!! Двигайся по поводу и без, главное не останавливайся!'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 27 and datetime.now().month == 4:
        bot.send_message(group_id, (f'И к слову, сегодня охуеть какой особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Алексей! И вы спросите: "тот Алексей который Саня?" - и я вам '
                                          f'отвечу: нет! Этот парень настолько легендарный, что его видно издалека. '
                                          f'Многие девушки/женщины могут делать ему миньет не вставая на колени, но они'
                                          f' его давно не интересуют.. В трудное время он мог бы быть солнечными '
                                          f'часами или глубиномером, но а пока он решил побыть глиномесом)). Леха с '
                                          f'днем рождения!!! Расти, качественно хавай и продолжай бежать так, как никто'
                                          f' никогда не бежал!'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 5 and datetime.now().month == 5:
        bot.send_message(group_id, f'''Господа, мне тут ебанный шар сообщил, что движение по Герценскому мосту перекрыто!!! 
А виновник всего этого Илюха, он же легендарный Филч! Обладатель фамилии на которую были забронированы все столики заведений Орла, 
а также способности вызывать умиление у самых непробиваемых девушек как молодого зала, так и женщин зала милф...жаль ему эта способность не нужна 
ибо он на другой стороне. Илюха с днем рождения!!! Выскакивай на челноке, но только не на Герценском мосту!''')
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 14 and datetime.now().month == 7:
        bot.send_message(group_id, (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто,но это'
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Диман, он же Маугли. Скрытый обитатель каменных джунглей, '
                                          f'который отрабатывает свои тактики подкатывания через третих лиц прикрываясь'
                                          f'женатостью, но мы то все прекрасно знаем какие цели он приследует на самом '
                                          f'деле)) Знает толк в кальянах и кальянщиках. Диман с днем рождения!!! '
                                          f'Достигай всех своих целей!'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 16 and datetime.now().month == 7:
        bot.send_message(group_id, (f' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это '
                                          f'ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого СерГей, да именно он вне всяких рейтингов и чартов, ведь даже в'
                                          f' его имени есть частица того, что согревало по ночам Фредди Меркьюри, Нила '
                                          f'Патрика Харриса и конечно же Бориса Моисеева. Серега с днем рождения!!! '
                                          f'Кайфуй, твори, созидай! Будь ласков как Басков.'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 8 and datetime.now().month == 9:
        bot.send_message(group_id, f''' Дорогие друзья! Все эти рейтинги и звания конечно очень круто, но это 
ежедневная рутина. Сегодня же особенный, ЛЕГЕНДАРНЫЙ день!!! А виновник всего этого Саня! Тот самый младший обитатель 
нашего сообщества, который мог бы качественно использовать опыт старших товарищей, но использовать особо нечего. Чтобы 
Саня себе не напланировал все закончится построением перетекающим в сон с мужиками. 
Саня с днем рождения!!! Кайфуй, не теряй время и скорее заканчивай шарагу!''')
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')
    elif datetime.now().day == 17 and datetime.now().month == 11:
        bot.send_message(group_id, (f' ВНИМАНИЕ! Мне тут сорока на хвосте принесла, что сегодня ЛЕГЕНДАРНЫЙ день!!! А виновник '
                                          f'всего этого Леха! Вы спросите: "тот самый длинный Леха?" - и я отвечу: нет!'
                                          f' Тот Леха, который Саня. И Скажу еще то, что длину своего роста и заодно '
                                          f'члена он компенсирует длиной тайма в ФИФЕ. Легендарный сомелье всего что '
                                          f'горит и просто пиздатый пацан. Леха с днем рождения!!! Пусть ФИФА длится '
                                          f'столько сколько тебе нужно брат!'))
        bot.send_message(group_id, 'твой подарок - https://www.youtube.com/watch?v=N6nJpNIK4PU')

    elif datetime.now().day == 31 and datetime.now().month == 12:
        bot.send_message(group_id, f'🚨🚨🚨Внимание!🚨🚨🚨 Пидр Клаус подводит итоги...\n'
                                   f'Кто же станет пидаром года?')
        file = open('gif_mr.Bin.mp4', 'rb')
        bot.send_animation(group_id, file)
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
        sh = gc.open("bot_statistic")
        worksheet = sh.get_worksheet(0)
        d1 = [(int(worksheet.acell('A1').value), "Филч"), (int(worksheet.acell('A2').value), "Игорь"),
              (int(worksheet.acell('A3').value), "Серега"), (int(worksheet.acell('A4').value), "Саня"),
              (int(worksheet.acell('A5').value), "Леха(Саня)"), (int(worksheet.acell('A6').value), "Леха(Фитиль)"),
              (int(worksheet.acell('A7').value), "Диман")]
        d1_sort = sorted(d1, reverse=True)
        bot.send_message(group_id, f'🍾🍾🍾ии.. им становится {d1_sort[0][1]}! Самый главный пидрила черезвычайно'
                                   f' пидарского года!!! {d1_sort[0][1]} прийми наши поздравления, а также '
                                   f'обязательства по амбоссадорству "Голубой устрицы". На ближайший год '
                                   f'на всех наших тусовках ты на разливе ибо больше всех заинтересован поскорее '
                                   f'споить пацанов. Тебе также полагается денежный приз в размере всех денег '
                                   f'накопленных в нашем фонде (в случае их отсутствия возмещаем глубоким '
                                   f'уважением. Хорошего нового года в новом статусе!')
        bot.send_message(group_id, f'За тобой приехали..')
        file = open('gif_zverev.mp4', 'rb')
        bot.send_animation(group_id, file)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    if callback.data == 'btn':
        file2 = open("важно.jpeg", 'rb')
        bot.send_photo(group_id, file2)
    if callback.data == 'bof':
        start_file = open("ball/start_image.png", 'rb')
        bot.send_photo(callback.message.chat.id, start_file)
        bot.send_message(callback.message.chat.id, '''Решил попытать удачу или просто переложить ответственность?
Что ж.. Чтобы все прошло как надо просто переведи сотку моему создателю на сбер и погладь шар''')
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but1 = types.KeyboardButton(text='Погладить шар')
        but2 = types.KeyboardButton(text='Шар съебись')
        kb1.add(but1, but2)
        bot.send_message(callback.message.chat.id, '...', reply_markup=kb1)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, ('Основные команды поддерживаемые ботом:\n'
                                        '/orel -  вызвать орловского помощника\n'
                                        '/pidorstat - пидорский рейтинг \n'
                                        '/start - инициализация бота\n'
                                        '/help - справка по боту\n'
                                        '/test - тестирование бота'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Бот уже инициализирован.
Я работаю по расписанию. Пидр дня назначается ежедневно 
в 11:00 по московскому времени

/help - справка по боту''')
    
    
@bot.message_handler(commands=['orel'])
def orel(message):
    bot.send_message(message.chat.id, 'Орловский помощник..', reply_markup=kb1)


@bot.message_handler(commands=['pidorstat'])
def test(message):
    bot.send_message(message.chat.id, pstat())


@bot.message_handler(commands=['test'])
def start(message):
    bot.send_message(message.chat.id, '''Протестируй себя петушок...А моя работа давно проверена и отлажена.

/help - справка по боту''')


@bot.message_handler(commands=['sent_message'])  # команда для переброски клиента из базы потенциальных клиентов в
def sent_message(message):    # базу старых клиентов
    if message.chat.id == admin_id:
        sent = bot.send_message(admin_id, 'Введите текст сообщения')
        bot.register_next_step_handler(sent, sent_message_perehvat)   # перехватывает ответ пользователя на сообщение "sent" и
                                                              # и направляет его аргументом в функцию base_perehvat
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав для использования данной команды')


@bot.message_handler(func=lambda v: v.text)
def chek_message(v):
    if v.text == 'Погладить шар':
        bot.send_photo(v.chat.id, ball_of_fate())
    if v.text == 'Шар съебись':
        kb2 = types.ReplyKeyboardRemove()
        bot.send_message(v.chat.id, '...', reply_markup=kb2)
    if 'Давинчи' in v.text:
        b = str(v.text).replace('Давинчи ', '', 1).replace('Давинчи, ', '', 1).replace('Давинчи,', '', 1).replace(
            ' Давинчи', '', 1)
        Davinci(bot, v, b)
    if 'давинчи' in v.text:
        b = str(v.text).replace('давинчи ', '', 1).replace('давинчи, ', '', 1).replace('давинчи,', '', 1).replace(
            ' давинчи', '', 1)
        Davinci(bot, v, b)


def sent_message_perehvat(message):
    bot.copy_message(group_id, admin_id, message.id)
    bot.send_message(admin_id, 'Сообщение отправлено!')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(pidr, "cron", day_of_week='mon-sun', hour=11)
    scheduler.start()

    
bot.infinity_polling()
