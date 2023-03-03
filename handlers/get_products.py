from aiogram import types
from db.base import get_products
from handlers.keyboards import get_start_ikb


async def grafik(message: types.Message):
    await message.reply(
        """
График работы: 
Понедельник - Пятница с 09:00 до 18:00 
Суббота с 10:00 до 17:00
Воскресенье - выходной

с 13:00 до 14:00 обеденный перерыв 
    """,
        reply_markup=get_start_ikb()
    )


async def cmd_product(callback: types.CallbackQuery):
    products = get_products()
    for product in products:
        with open(product[3], 'rb') as image:
            await callback.message.answer_photo(
                photo=image,
                caption=f'{product[1]}\n'
                        f'Цена: {product[2]}'
            )
