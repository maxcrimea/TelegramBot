from aiogram import types


async def products(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["JavaScript", "Python"]
    kb.add(*buttons)
    await message.answer("Запишитесь на пробный урок!", reply_markup=kb)
