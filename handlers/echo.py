from os import listdir
from random import choice
from aiogram import types


async def picture(message: types.Message):
    images = listdir("images")
    image = choice(images)
    with open(f"images/{image}", "rb") as cat:
        await message.answer_photo(
            photo=cat,
            caption='лови котика!'
        )


async def myinfo(message: types.Message):
    await message.answer(
        f"""
        /Ваш id: {message.from_user.id}
    /Ваш nickname: {message.from_user.first_name}
    /Ваш username: {message.from_user.username}
        """
    )


async def echo(message: types.Message):
    if len(message.text.split()) > 2:
        await message.answer(
            message.text.upper()
        )
