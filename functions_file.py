# библиотека работы с гугл таблицами
# import gspread
import openai
# библиотека проверки даты
# from datetime import datetime
from paswords import *

saved_messages_davinci = []


async def Davinci(bot, message, text):
    try:
        openai.api_key = Davinci_key
        answer_davinci = open('davinci.txt.txt', 'r', encoding='utf-8')
        saved_messages_davinci.insert(0, f'Вы: {text}\n')
        prompt_davinci = (str(answer_davinci.read()) + ''.join(reversed(saved_messages_davinci)))

        answer_message = await bot.send_message(message.chat.id, f'секунду..')
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt_davinci,
            temperature=0.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
      #  await bot.edit_message_text(message.chat.id, f'{response["choices"][0]["text"]}')
        await bot.edit_message_text(f'{response["choices"][0]["text"]}', message.chat.id, answer_message.message_id)
        saved_messages_davinci.insert(0, f'{str(response["choices"][0]["text"])}\n')
        if len(saved_messages_davinci) >= 8:
            del saved_messages_davinci[3:]
    except Exception:
        await bot.send_message(message.chat.id, "Простите но мне нужен перекур..")
        await bot.send_message(admin_id, "Простите но мне нужен перекур..")
        del saved_messages_davinci[1:]



