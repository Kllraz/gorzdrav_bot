from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Group, SwitchTo
from aiogram_dialog.widgets.text import Jinja, Const

from bot import keyboard_texts
from bot.utils.buttons import get_menu_button
from ..states import TrackingStates

WINDOW_NAME = "tracking_deleted"
SHOW_TRACKING_BTN_ID = f"{WINDOW_NAME}_show_tracking_btn"

window = Window(
    Jinja("tracking/deleted_header.html"),
    Group(
        SwitchTo(
            text=Const(keyboard_texts.general.SHOW_TRACKING),
            id=SHOW_TRACKING_BTN_ID,
            state=TrackingStates.list
        ),
        get_menu_button(),
        width=2
    ),
    state=TrackingStates.deleted,
)
