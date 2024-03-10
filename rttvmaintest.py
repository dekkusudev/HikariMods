from hikkatl.types import Message
from .. import loader, utils

@loader.tds
class MyNewModule(loader.Module):
    """My New Rules Module"""
    strings = {"name": "MyNewModule", 
               "rules": """<b><i>‼️ ПРАВИЛА</i></b>

1. Запрещен сильный оффтоп — мут до 8 часов
2. Запрещена чернуха, 18+ и мерзкий контент — бан
3. Запрещен спам — мут до 24 часов
4. Запрещен сильный флуд — мут до 12 часов
5. Запрещена реклама, самопиар (приглашения через лс так же считаются) — бан/мут до 48 часов по усмотрению модератора"""}

    @loader.command(
        pattern="^/rules$",
        ru_doc="Правила чата"
    )
    async def rules(self, message: Message):
        """Send chat rules"""
        await utils.answer(message, self.strings("rules"))
