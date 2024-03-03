from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

@Client.on_message(filters.command("offchat") & filters.me)
async def restrict_chat(client, message):
    if message.chat.type not in ["supergroup", "channel"]:
        await message.reply("Я могу ограничивать только супергруппы и каналы")
        return

    # Получить информацию о чате
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)

    # Проверить, является ли пользователь администратором
    admins = await client.get_chat_members(chat_id, filter="administrators")
    user_id = message.from_user.id
    user_is_admin = any(admin.user.id == user_id for admin in admins)

    if not user_is_admin:
        await message.reply("Вы должны быть администратором, чтобы ограничить чат")
        return

    # Установка разрешений на чат
    await client.set_chat_permissions(chat_id, ChatPermissions())
    await message.reply(f"Чат {chat.title} закрыт на ночь. Писать могут только администраторы")

@Client.on_message(filters.command("soffchat") & filters.me)
async def restrict_chat(client, message):
    if message.chat.type not in ["supergroup", "channel"]:
        await message.reply("Я могу ограничивать только супергруппы и каналы")
        return

    # Получить информацию о чате
    chat_id = message.chat.id
    chat = await client.get_chat(chat_id)

    # Проверить, является ли пользователь администратором
    admins = await client.get_chat_members(chat_id, filter="administrators")
    user_id = message.from_user.id
    user_is_admin = any(admin.user.id == user_id for admin in admins)

    if not user_is_admin:
        await message.reply("Вы должны быть администратором, чтобы ограничить чат")
        return

    # Установка разрешений на чат
    await client.set_chat_permissions(chat_id, ChatPermissions())
    await message.reply(f"Чат {chat.title} закрыт. Писать могут только администраторы")

