from hikkatl.types import *
from .. import loader, utils

@loader.tds
class MyNewInlineModule(loader.Module):
    """My New Inline Rules Module"""
    strings = {"name": "MyNewInlineModule", 
               "rules": """<b><i>‼️ ПРАВИЛА</i></b>

1. Запрещен сильный оффтоп — мут до 8 часов
2. Запрещена чернуха, 18+ и мерзкий контент — бан
3. Запрещен спам — мут до 24 часов
4. Запрещен сильный флуд — мут до 12 часов
5. Запрещена реклама, самопиар (приглашения через лс так же считаются) — бан/мут до 48 часов по усмотрению модератора"""}

    @loader.inline
    async def inline_rules(self, event: InlineQuery.Event):
        """Responds to inline query with chat rules"""
        builder = event.builder
        await event.answer([
            builder.article(
                title="Правила чата",
                description=self.strings("rules"),
                text=self.strings("rules")
            )
        ])
