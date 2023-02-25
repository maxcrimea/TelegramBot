from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_start_ikb() -> InlineKeyboardMarkup:
    button = [
        InlineKeyboardButton(text='Просмотр всех продуктов', callback_data='get_all')
        ]
    ikb = InlineKeyboardMarkup(row_width=1)
    ikb.add(*button)
    return ikb