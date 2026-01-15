import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db import engine
from models_db import Base
from handlers.start import register_start_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# подключаем обработчики
register_start_handlers(dp)


async def main():
    # создаём таблицы (если нет)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    logging.info("🤖 Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")
