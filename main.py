from aiogram import executor
from config import dp
from handlers.echo import echo, picture, myinfo
from handlers.start import (
    start,
    cmd_help,
)
from handlers.products import (
    products
)

if __name__ == "__main__":
    print(__name__)
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(picture, commands=["picture"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(products, commands=["products"])
    dp.register_message_handler(echo)
    executor.start_polling(dp)
