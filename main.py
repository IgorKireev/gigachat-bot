"""Модуль main.py запускает Telegram-бота на основе Aiogram."""

import asyncio
from aiogram import Bot, Dispatcher
import config
from app.handlers import router


async def main():
    """
    Запускает бота на основе Aiogram.

    Создаёт объект Bot и Dispatcher, подключает маршрутизатор обработчиков и запускает
    пуллинг для получения обновлений от Telegram.

    :return: None
    :rtype: None
    """
    bot = Bot(config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
