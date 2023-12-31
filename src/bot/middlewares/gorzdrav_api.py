from typing import Callable, Dict, Awaitable, Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from src.bot.structures import TransferStruct
from src.gorzdrav_api import GorZdravAPI


class GorZdravAPIMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: TransferStruct
                       ) -> Any:
        async with GorZdravAPI() as api:
            data["gorzdrav_api"] = api
            return await handler(event, data)
