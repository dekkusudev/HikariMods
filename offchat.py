from hikkatl.types import Message
from pyrogram import filters
from pyrogram.types import ChatPermissions
from .. import loader, utils

@loader.tds
class MyModule(loader.Module):
    """OffChat"""
    strings = {"name": "OffChat",
               "not_supergroup": "Я могу ограничивать только супергруппы и каналы",
               "not_admin": "Вы должны быть администратором, чтобы ограничить чат",
               "chat_closed_night": "Чат {} закрыт на ночь. Писать могут только администраторы",
               "chat_closed": "Чат {} закрыт. Писать могут только администраторы"}

    @loader.command(pattern="offchat")
    async def offchat(self, message: Message):
        """Close chat at night"""
        if message.chat.type not in ["supergroup", "channel"]:
            await utils.answer(message, self.strings("not_supergroup"))
            return

        chat_id = message.chat.id
        chat = message.chat

        # Get chat admins
        admins = await message.client.get_chat_members(chat_id, filter="administrators")
        user_id = message.from_user.id
        user_is_admin = any(admin.user.id == user_id for admin in admins)

        if not user_is_admin:
            await utils.answer(message, self.strings("not_admin"))
            return

        # Set chat permissions
        permissions = ChatPermissions()
        await message.client.set_chat_permissions(chat_id, permissions)
        await utils.answer(message, self.strings("chat_closed_night").format(chat.title))

    @loader.command(pattern="soffchat")
    async def soffchat(self, message: Message):
        """Close chat"""
        if message.chat.type not in ["supergroup", "channel"]:
            await utils.answer(message, self.strings("not_supergroup"))
            return

        chat_id = message.chat.id
        chat = message.chat

        # Get chat admins
        admins = await message.client.get_chat_members(chat_id, filter="administrators")
        user_id = message.from_user.id
        user_is_admin = any(admin.user.id == user_id for admin in admins)

        if not user_is_admin:
            await utils.answer(message, self.strings("not_admin"))
            return

        # Set chat permissions
        permissions = ChatPermissions()
        await message.client.set_chat_permissions(chat_id, permissions)
        await utils.answer(message, self.strings("chat_closed").format(chat.title))
