from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]


def get_start_choice_keyboard() -> types.InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🎯 Choose level manually", callback_data="choice:manual")
    kb.button(text="📝 Take a placement test", callback_data="choice:test")
    kb.adjust(1)
    return kb.as_markup()


def get_levels_keyboard() -> types.InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for lvl in LEVELS:
        kb.button(text=lvl, callback_data=f"level:{lvl}")
    kb.adjust(3)
    return kb.as_markup()
