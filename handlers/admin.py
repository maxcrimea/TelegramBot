import string
import json
from aiogram import types

banned_users = []


async def is_admin(message: types.Message):
    """
    проверка является ли автор сообщения админом данного чата
    """
    print(message.from_user)
    author = message.from_user.id
    admins = await message.chat.get_administrators()
    not_admin = False
    for admin in admins:
        if admin['user']['id'] == author:
            not_admin = True
            break
    return not_admin


async def check_bad_words(message: types.Message):
    """
    проверка содержит ли сообщение пользователя слово "мат"
    """
    buttons = [
        types.InlineKeyboardMarkup(text='ответьте "/да"', callback_data='да')
    ]
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(*buttons)
    admin_author = await is_admin(message)
    abuser_id = message.from_user.id
    if message.chat.type != 'private':
        if not admin_author:
            if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
                    .intersection(set(json.load(open('cenz.json')))) != set():
                banned_users.append(abuser_id)
                print(banned_users)
                await message.reply(
                    f'кикнуть пользователя {message.from_user.first_name} за иcпользование нехороших слов?',
                    reply_markup=kb
                )


async def ban_user(message: types.Message):
    """
    обработчик, чтоб банить пользователя в чате
    через команду
    """
    if message.chat.type != 'private':
        admin_author = await is_admin(message)
        print(f"{admin_author=}")
        if admin_author and message.reply_to_message:
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=banned_users[-1]
            )
        return banned_users.clear()
