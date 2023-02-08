from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv, listdir
from random import choice

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user.first_name
    await message.answer(
        f'Привет, {user}'
    )


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(
        """
        /start - для старта бота
        /help - вы сейчас здесь
        /myinfo - ваши данные
        /picture - рандомный котик
        """
    )


@dp.message_handler(commands='myinfo')
async def myinfo(message: types.Message):
    await message.answer(
        f"""
        /Ваш id: {message.from_user.id}
        /Ваш nickname: {message.from_user.first_name}
        /Ваш username: {message.from_user.username}
        """
    )


@dp.message_handler(commands='picture')
async def picture(message: types.Message):
    images = listdir("images")
    image = choice(images)
    with open(f"images/{image}", "rb") as cat:
        await message.answer_photo(
            photo=cat,
            caption='лови котика'
        )


@dp.message_handler()
async def echo(message: types.Message):
    if len(message.text.split()) > 2:
        await message.answer(
            message.text.upper()
        )


executor.start_polling(dp)
