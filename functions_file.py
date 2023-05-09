# библиотека работы с гугл таблицами
# import gspread
import openai
# библиотека проверки даты
# from datetime import datetime
from openpyxl import load_workbook  # библиотека работы с exel таблицами
from paswords import *

saved_messages_davinci = []


async def Davinci(bot, message, text, answer_message, proverka):
    global statistic
    try:
        openai.api_key = Davinci_key
        answer_davinci = open('davinci.txt.txt', 'r', encoding='utf-8')
        saved_messages_davinci.insert(0, f'Вы: {text}\n')
        prompt_davinci = (str(answer_davinci.read()) + ''.join(reversed(saved_messages_davinci)))
        if proverka == 'YES':
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt_davinci,
                temperature=0.0,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            await bot.edit_message_text(f'{response["choices"][0]["text"]}', message.chat.id, answer_message.message_id)
            saved_messages_davinci.insert(0, f'{str(response["choices"][0]["text"])}\n')
            if len(saved_messages_davinci) >= 8:
                del saved_messages_davinci[3:]
        else:
            await bot.edit_message_text(f'Для дальнейшего использования бота нужно пополнить баланс', message.chat.id,
                                        answer_message.message_id)
    except Exception:
        await bot.send_message(message.chat.id, "Простите но мне нужен перекур..")
        await bot.send_message(admin_id, "Простите но мне нужен перекур..")
        del saved_messages_davinci[1:]


class statistic:
    def __init__(self):
        self.wb = load_workbook('chek_list.xlsx')
        self.ws = self.wb['посещения']

    async def obnulenie(self):
        for row in self.ws['B2':f'C{self.ws.max_row}']:
            if row[1].value != 0:
                row[1].value = int(row[1].value) - 1
                row[0].value = 0
            else:
                row[0].value = 0
        self.wb.save('chek_list.xlsx')

    # def plus_one(self):
    #     self.worksheet.update('A2', str(int(self.worksheet.acell('A2').value) + 1))
    #     self.worksheet.update('B2', str(int(self.worksheet.acell('B2').value) + 1))
    #     self.worksheet.update('C2', str(int(self.worksheet.acell('C2').value) + 1))
    #     self.worksheet.update('D2', str(int(self.worksheet.acell('D2').value) + 1))

    async def proverka(self, message):
        for row in self.ws['A2':f'C{self.ws.max_row}']:
            if row[0].value == message.chat.id:
                if row[2].value != 0:
                    return 'YES'
                else:
                    if row[1].value <= 2:
                        row[1].value += 1
                        self.wb.save('chek_list.xlsx')
                        return 'YES'
                    else:
                        return "NO"
        new_row = self.ws.max_row + 1
        self.ws[f'A{new_row}'].value = message.chat.id
        self.ws[f'B{new_row}'].value = 1
        self.ws[f'C{new_row}'].value = 0
        self.wb.save('chek_list.xlsx')
        return 'YES'




