from hikkatl.types import Message
from .. import loader, utils

@loader.tds
class MyModule(loader.Module):
    """My Rules Module"""
    strings = {"name": "RulesModule", 
               "rules": """‼️ ПРАВИЛА

1. Запрещен сильный оффтоп — мут до 8 часов
2. Запрещена чернуха, 18+ и мерзкий контент — бан
3. Запрещен спам — мут до 24 часов
4. Запрещен сильный флуд — мут до 12 часов
5. Запрещена реклама, самопиар (приглашения через лс так же считаются) — бан/мут до 48 часов по усмотрению модератора"""}

    @loader.command(
        ru_doc="Правила чата"
    )
    async def rules(self, message: Message):
        """Send chat rules"""
        await utils.answer(message, self.strings("rules"))
