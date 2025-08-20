"""Модуль get_or_upd_giga_token содержит функцию для получения и обновления токена GigaChat."""

import config
from app.connect_redis import set_value, get_value
from app.gigachat import get_token


async def get_or_update_token():
    """
    Получает токен GigaChat из Redis или обновляет его через API.

    :return: Токен для доступа к GigaChat API.
    :rtype: str
    """
    giga_token = await get_value()
    if giga_token:
        return giga_token
    giga_token = await get_token(config.AUTH_KEY)
    await set_value(giga_token)
    return giga_token
