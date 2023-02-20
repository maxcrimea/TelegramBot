from aiogram import types


async def start(message: types.Message):
    user = message.from_user.first_name
    buttons = [
        types.InlineKeyboardButton(text="Посетите наш веб сайт!",
                                   url="https://geektech.kg"),
        types.InlineKeyboardButton(text="Приходите к нам в гости!",
                                   url="https://go.2gis.com/9d01se")
    ]
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*buttons)
    await message.answer(
        f'Привет, {user}',
        reply_markup=kb
    )


async def cmd_help(message: types.Message):
    await message.answer(
        """
        /start - для старта бота
    /help - вы сейчас здесь
    /myinfo - ваши данные
    /picture - рандомный котик
    /products - наши курсы
        """
    )
