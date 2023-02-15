from aiogram import executor
from config import dp
from handlers.echo import picture, myinfo
from handlers.start import (
    start,
    cmd_help,
)
# from handlers.products import (
#     products, catch_products
# )
from handlers.admin import check_bad_words, ban_user

if __name__ == "__main__":
    print(__name__)
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(picture, commands=["picture"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    dp.register_message_handler(ban_user, commands=["да"], commands_prefix='!,/')
    # dp.register_message_handler(products)
    # dp.register_message_handler(catch_products)
    # dp.register_message_handler(echo)
    dp.register_message_handler(check_bad_words)

    executor.start_polling(dp, skip_updates=True)
