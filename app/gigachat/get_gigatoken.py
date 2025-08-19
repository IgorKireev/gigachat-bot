"""Модуль get_gigatoken содержит функцию для получения access-токена для GigaChat API."""

import httpx
import uuid


async def get_token(auth_token: str, scope: str = "GIGACHAT_API_PERS"):
    """
    Получает OAuth-токен для доступа к GigaChat API.
    Отправляет POST-запрос к эндпоинту аутентификации с указанным `auth_token` и `scope`.
    Возвращает access_token для дальнейшего использования при запросах к GigaChat.

    :param auth_token: Базовый токен авторизации (Basic Auth).
    :type auth_token: str
    :param scope: Область доступа токена (по умолчанию 'GIGACHAT_API_PERS').
    :type scope: str
    :return: Access token для использования в API GigaChat.
    :rtype: str
    """
    rq_uid = str(uuid.uuid4())
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "RqUID": rq_uid,
        "Authorization": f"Basic {auth_token}",
    }
    payload = {"scope": scope}
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.request(
                method="POST", url=url, headers=headers, data=payload
            )
            return response.json()["access_token"]
    except Exception as e:
        print(f"Ошибка: {str(e)}")
