from aiogram import types


class buttons:  # класс для создания клавиатур различных категорий товаров

    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    async def menu_buttons(self):
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        but1 = types.KeyboardButton(text='Мой статус 🤘🏻')
        but2 = types.KeyboardButton(text='Инструкция 📋')
        but3 = types.KeyboardButton(text='О нас ⁉️')
        but4 = types.KeyboardButton(text='Пример использования ✅')
        but5 = types.KeyboardButton(text='Оформить подписку 💵')
        kb1.add(but1, but2, but3, but4, but5)
        await self.bot.send_message(self.message.chat.id, text='...', reply_markup=kb1)

    async def oplata_buttons(self, url):
        kb5 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Безлимит на сутки(100 руб)!',
                                          url=url)
        but2 = types.InlineKeyboardButton(text='Проверить платеж', callback_data='Оплачено')
        kb5.add(but1, but2)
        try:
            await self.bot.send_message(self.message.chat.id, f'Оформить подписку\n '
                                                              f'/help - справка по боту', reply_markup=kb5)
        except AttributeError:
            await self.bot.send_message(self.message.message.chat.id, f'Оформить подписку\n '
                                                                      f'/help - справка по боту', reply_markup=kb5)