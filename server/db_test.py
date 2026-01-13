import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

DB_URL = "postgresql+asyncpg://postgres:123456@localhost:5433/tutor_db"

async def check_connection():
    print(f"Попытка подключения к {DB_URL}...")
    engine = create_async_engine(DB_URL)
    
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT version();"))
            version = result.scalar()
            print("✅ Успех! База данных на связи.")
            print(f"Версия PostgreSQL: {version}")
    except Exception as e:
        print("❌ Ошибка подключения!")
        print(f"Детали: {e}")
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(check_connection())
