from aiogram import types
from config import scheduler, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class NotifierForm(StatesGroup):
    text = State()
    hour = State()
    minutes = State()


async def notifier_text(message: types.Message, state: FSMContext):
    """
    функция тригерится на "напомнить", сохраняет остальной текст
    и запускает состояние
    """
    await NotifierForm.text.set()
    text = message.text.replace('напомнить ', '')
    async with state.proxy() as data:
        data['text'] = text
    await NotifierForm.next()
    await message.answer("Во сколько часов?")


async def notifier_hour(message: types.Message, state: FSMContext):
    """
    сохраняет запрашиваемый у пользователя час
    и запускает состояние
    """
    hour = message.text
    if not hour.isnumeric():
        await message.reply("Вводите только цифры")
    elif int(hour) < 0 or int(hour) > 23:
        await message.reply("Введите корректно во сколько часов!")
    else:
        async with state.proxy() as data:
            data['hour'] = hour
            await NotifierForm.next()
            await message.answer("Во сколько минут?")


async def notifier_minutes(message: types.Message, state: FSMContext):
    """
    сохраняет запрашиваемые у пользователя минуты
    и запускает напоминалку
    """
    minutes = message.text
    if not minutes.isnumeric():
        await message.reply("Вводите только цифры")
    elif int(minutes) < 0 or int(minutes) > 59:
        await message.reply("Введите корректно во сколько часов!")
    else:
        async with state.proxy() as data:
            data['minutes'] = minutes
            print(data)
            text = data['text']
            minutes = int(data['minutes'])
            hour = int(data['hour'])

    await message.answer(f"ok, напомню {text} в {hour}:{minutes}")
    await state.finish()

    async def notify(user_id: int):
        await bot.send_message(
            text=f'не забудь {text}',
            chat_id=user_id
        )

    scheduler.add_job(notify, 'cron', hour=hour, minute=minutes, args=(message.from_user.id,))
