from aiogram import types
from config import scheduler, bot


async def process_text(message: types.Message):
    """
    Сохраняем текст напоминалки без слова "напомнить",
    далее вызываем напоминалку с заданным интервалом
    """
    text = message.text.split(' ', 1)[1]
    await message.answer("Принято!")

    async def notify(user_id: int):
        await bot.send_message(
            text=text,
            chat_id=user_id
        )

    scheduler.add_job(notify, 'interval', seconds=5, args=(message.from_user.id,))
