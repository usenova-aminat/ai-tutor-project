from aiogram import types, F
from aiogram.filters import CommandStart
from sqlalchemy import select, update

from db import async_session
from models_db import User
from keyboards import get_start_choice_keyboard, get_levels_keyboard, LEVELS


def register_start_handlers(dp):
    @dp.message(CommandStart())
    async def cmd_start(message: types.Message):
        tg_id = message.from_user.id
        username = message.from_user.username

        async with async_session() as session:
            result = await session.execute(select(User).where(User.tg_id == tg_id))
            user = result.scalar_one_or_none()

            if not user:
                session.add(User(tg_id=tg_id, username=username))  # default A1
                await session.commit()

                await message.answer(
                    "Hi! 👋 I’m your AI Tutor.\nHow would you like to set your level?",
                    reply_markup=get_start_choice_keyboard()
                )
                return

            await message.answer(
                f"Welcome back! ✅\nYour current level: **{user.level}**",
                parse_mode="Markdown"
            )

    @dp.callback_query(F.data == "choice:manual")
    async def process_manual_choice(callback: types.CallbackQuery):
        await callback.message.edit_text(
            "Great — choose your current level:",
            reply_markup=get_levels_keyboard()
        )
        await callback.answer()

    @dp.callback_query(F.data == "choice:test")
    async def process_test_choice(callback: types.CallbackQuery):
        await callback.message.edit_text(
            "🛠 The placement test is under development.\n"
            "For now, please choose your level manually:",
            reply_markup=get_levels_keyboard()
        )
        await callback.answer()

    @dp.callback_query(F.data.startswith("level:"))
    async def on_level_selected(callback: types.CallbackQuery):
        level = callback.data.split(":", 1)[1]
        tg_id = callback.from_user.id

        if level not in LEVELS:
            await callback.answer("Unknown level", show_alert=True)
            return

        async with async_session() as session:
            await session.execute(update(User).where(User.tg_id == tg_id).values(level=level))
            await session.commit()

        await callback.message.edit_text(
            f"✅ Saved! Your level is now: **{level}**",
            parse_mode="Markdown",
        )
        await callback.answer("Level updated ✅")
