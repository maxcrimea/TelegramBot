from aiogram import executor
from aiogram.dispatcher.filters import Text
import logging

from config import dp, scheduler
from handlers.echo import picture, myinfo
from handlers.start import (
    start,
    cmd_help,
)
from handlers.user_info_fsm import (
    UserForm,
    start_user_dialog,
    process_age,
    process_name,
    process_address,
    process_day,
    mail,
    not_mail
)

from db.base import (
    db_init,
    delete_tables,
    create_tables,
    populate_products
)


from handlers.products import (
    products, catch_products
)
from handlers.admin import check_bad_words, ban_user_warning, ban_user
from handlers.notifier import (
    NotifierForm,
    notifier_text,
    notifier_hour,
    notifier_minutes
)
from handlers.get_products import (
    cmd_product,
    grafik
)


async def startup(_):
    db_init()
    delete_tables()
    create_tables()
    populate_products()


if __name__ == "__main__":
    print(__name__)
    logging.basicConfig(level=logging.INFO)
    # dp.register_message_handler(start_user_dialog, commands=["form"])
    # dp.register_message_handler(process_name, state=UserForm.name)
    # dp.register_message_handler(process_age, state=UserForm.age)
    # dp.register_message_handler(process_address, state=UserForm.address)
    # dp.register_message_handler(process_day, state=UserForm.day)
    # dp.register_callback_query_handler(mail, Text(startswith="да"))
    # dp.register_callback_query_handler(not_mail, Text(startswith="нет"))
    dp.register_message_handler(notifier_text, Text(startswith=["напомнить"]))
    dp.register_message_handler(notifier_hour, state=NotifierForm.hour)
    dp.register_message_handler(notifier_minutes, state=NotifierForm.minutes)
    dp.register_callback_query_handler(cmd_product, Text(startswith=["get_all"]))
    dp.register_message_handler(start, commands=["start"])
    dp.register_message_handler(grafik, commands=["product"])
    dp.register_message_handler(cmd_help, commands=["help"])
    dp.register_message_handler(picture, commands=["picture"])
    dp.register_message_handler(myinfo, commands=["myinfo"])
    # dp.register_message_handler(ban_user, commands=["да"], commands_prefix='!,/')
    # dp.register_message_handler(products)
    # dp.register_message_handler(catch_products)
    # dp.register_message_handler(echo)
    # dp.register_message_handler(check_bad_words)
    # dp.register_callback_query_handler(ban_user_warning, Text(startswith="abuser_name_warning"))
    # dp.register_callback_query_handler(ban_user, Text(startswith="abuser_id"))

    scheduler.start()
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=startup)
