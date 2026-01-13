import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from models_db import Base, User   # ✅ ВАЖНО: правильный импорт

# --- НАСТРОЙКИ ---
BOT_TOKEN = "8513323651:AAGWfP3s3f5R8RawE1Yj37vXMiSD6NL18rU"
DATABASE_URL = "postgresql+asyncpg://postgres:123456@localhost:5433/tutor_db"

# --- БАЗА ДАННЫХ ---
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# --- БОТ ---
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.tg_id == message.from_user.id)
        )
        user = result.scalar_one_or_none()

        if not user:
            user = User(
                tg_id=message.from_user.id,
                username=message.from_user.username
            )
            session.add(user)
            await session.commit()

            text = (
                f"Привет, {message.from_user.first_name}! 👋\n"
                f"Я зарегистрировал тебя. Твой уровень: A1."
            )
        else:
            text = (
                f"С возвращением, {message.from_user.first_name}! ✨\n"
                f"Твой текущий уровень: {user.level}."
            )

        await message.answer(text)

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("🤖 Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
