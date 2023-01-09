# библиотека работы с гугл таблицами
import gspread
import openai
# библиотека проверки даты
from datetime import datetime
# библиотека рандома
from random import *
from paswords import *


# функция открывает гугл таблицу статистики, начисляет балл и возвращает новое значение
def value_plus_one(j):
    gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
    sh = gc.open("bot_statistic")
    worksheet = sh.get_worksheet(0)
    worksheet.update(j, str(int(worksheet.acell(j).value) + 1))


# функция открывает гугл таблицу статистики и возвращает все значения в отсортированном виде
def pstat():
    gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
    sh = gc.open("bot_statistic")
    worksheet = sh.get_worksheet(0)
    d1 = [(int(worksheet.acell('A1').value), "Филч"), (int(worksheet.acell('A2').value), "Игорь"),
          (int(worksheet.acell('A3').value), "Серега"), (int(worksheet.acell('A4').value), "Саня"),
          (int(worksheet.acell('A5').value), "Леха(Саня)"), (int(worksheet.acell('A6').value), "Леха(Фитиль)"),
          (int(worksheet.acell('A7').value), "Диман")]
    d1_sort = sorted(d1, reverse=True)
    return (f'''РЕЙТИНГ ПИДАРАСОВ:

1. {d1_sort[0][1]} -----> {d1_sort[0][0]} раз(а)
2. {d1_sort[1][1]} -----> {d1_sort[1][0]} раз(а)
3. {d1_sort[2][1]} -----> {d1_sort[2][0]} раз(а)
4. {d1_sort[3][1]} -----> {d1_sort[3][0]} раз(а)
5. {d1_sort[4][1]} -----> {d1_sort[4][0]} раз(а)
6. {d1_sort[5][1]} -----> {d1_sort[5][0]} раз(а)
7. {d1_sort[6][1]} -----> {d1_sort[6][0]} раз(а)

Да здравствует наш чемпион {d1_sort[0][1]}! Его результативности 
может позавидовать Элтон Джон и другие Великие. Пожелаем
ему здоровья, успехов в личной жизни и новыйх побед.

/help - справка по боту''')


# функция обнуляющая все значения статистики в первый день нового месяца
def obnulenie_stat():
    if datetime.now().day == 1:
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')
        sh = gc.open("bot_statistic")
        worksheet = sh.get_worksheet(0)
        worksheet.update('A1:A7', [[0], [0], [0], [0], [0], [0], [0]])


# функция шара судьбы
def ball_of_fate():
    ball_choice = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    if ball_choice == 1:
        ball_answer = open("ball/var_one.png", 'rb')
        return ball_answer
    if ball_choice == 2:
        ball_answer = open("ball/var_two.png", 'rb')
        return ball_answer
    if ball_choice == 3:
        ball_answer = open("ball/var_tree.png", 'rb')
        return ball_answer
    if ball_choice == 4:
        ball_answer = open("ball/var_four.png", 'rb')
        return ball_answer
    if ball_choice == 5:
        ball_answer = open("ball/var_five.png", 'rb')
        return ball_answer
    if ball_choice == 6:
        ball_answer = open("ball/var_six.png", 'rb')
        return ball_answer
    if ball_choice == 7:
        ball_answer = open("ball/var_seven.png", 'rb')
        return ball_answer
    if ball_choice == 8:
        ball_answer = open("ball/var_eight.png", 'rb')
        return ball_answer
    if ball_choice == 9:
        ball_answer = open("ball/var_nine.png", 'rb')
        return ball_answer
    if ball_choice == 10:
        ball_answer = open("ball/var_ten.png", 'rb')
        return ball_answer
    if ball_choice == 11:
        ball_answer = open("ball/var_eleven.png", 'rb')
        return ball_answer


class Davinci:
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message
        openai.api_key = Davinci_key

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.message.text[8:],
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        self.bot.send_message(message.chat.id, f'секунду..')
        self.bot.send_message(message.chat.id, f'{response["choices"][0]["text"]}')
