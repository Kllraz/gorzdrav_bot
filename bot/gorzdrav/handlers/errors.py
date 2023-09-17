from aiogram import Router
from aiogram.filters import ExceptionTypeFilter
from aiogram.types import ErrorEvent

from bot import bot_asnwers
from gorzdrav_api.exceptions import ServerError

router = Router()


@router.error(ExceptionTypeFilter(ServerError))
async def server_error_handler(event: ErrorEvent):
    if event.update.message:
        chat_id = event.update.message.from_user.id
    else:
        chat_id = event.update.callback_query.from_user.id

    await event.update.bot.send_message(chat_id=chat_id, text=bot_asnwers.GORZDRAV_ERROR)