from aiogram import Router, types
from aiogram.filters import Command

from bot.gorzdrav.keyboards.inline import tracking_paginator_items_factory
from bot.utils.inline_paginator import Paginator
from bot.utils.template_engine import render_template
from database.database import Repository

router = Router()


@router.message(Command("tracking"))
async def tracking_handler(message: types.Message, repository: Repository):
    tracking = await repository.get_user_tracking(tg_user_id=message.from_user.id)
    texts, buttons = tracking_paginator_items_factory(tracking)

    paginator = Paginator(
        router=router,
        name="tracking",
        header_text=render_template("gorzdrav/tracking/tracking_header.html"),
        buttons=buttons,
        texts=texts
    )

    await paginator.send_paginator(message)