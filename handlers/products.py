from aiogram import types


async def products(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["JavaScript", "Python"]
    kb.add(*buttons)
    await message.answer("Запишитесь на пробный урок!", reply_markup=kb)


async def catch_products(message: types.Message):
    if message.text == "JavaScript":
        await message.answer("Запишитесь на пробный урок на frontend!")
    elif message.text == "Python":
        await message.answer("Запишитесь на пробный урок на backend!")