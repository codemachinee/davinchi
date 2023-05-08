# библиотека работы с гугл таблицами
import gspread
import openai
# библиотека проверки даты
from datetime import datetime
from paswords import *

saved_messages_davinci = []
saved_messages_artur = []


class Davinci:
    global saved_messages_davinci

    def __init__(self, bot, message, text):
        try:
            self.bot = bot
            self.message = message
            self.text = text
            openai.api_key = Davinci_key
            answer_davinci = open('davinci.txt', 'r', encoding='utf-8')
            saved_messages_davinci.insert(0, f'Вы: {self.text}\n')
            prompt_davinci = (str(answer_davinci.read()) + ''.join(reversed(saved_messages_davinci)))
            self.bot.send_message(message.chat.id, f'секунду..')

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt_davinci,
                temperature=0.3,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            self.bot.send_message(message.chat.id, f'{response["choices"][0]["text"]}')
            saved_messages_davinci.insert(0, f'{str(response["choices"][0]["text"])}\n')
            if len(saved_messages_davinci) >= 8:
                del saved_messages_davinci[3:]
        except Exception:
            self.bot.send_message(message.chat.id, "Простите но мне нужен перекур..")
            del saved_messages_davinci[1:]



