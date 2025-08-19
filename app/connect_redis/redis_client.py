"""Модуль connect_redis содержит функции для работы с Redis."""

import redis.asyncio as redis
import config


redis_client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)


async def set_value(value: str):
    """
    Сохраняет токен GigaChat в Redis с истечением через 30 минут.

    :param value: Токен GigaChat для сохранения.
    :type value: str
    :return: None
    :rtype: None
    """
    await redis_client.set("giga_token", value, ex=30 * 60)


async def get_value():
    """
    Получает токен GigaChat из Redis.

    :return: Токен GigaChat или None.
    :rtype: str | None
    """
    val = await redis_client.get("giga_token")
    if val is not None:
        return val.decode()
    return None
