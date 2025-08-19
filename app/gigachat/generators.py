"""Модуль generators содержит функцию для общения с GigaChat API."""

import httpx


async def communication(auth_token: str, message: str):
    """
    Отправляет сообщение пользователю в GigaChat и возвращает ответ.

    :param auth_token: Токен доступа для GigaChat API.
    :type auth_token: str
    :param message: Сообщение пользователя для передачи в GigaChat.
    :type message: str
    :return: Ответ GigaChat на сообщение пользователя.
    :rtype: str
    """
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.request(
            method="POST",
            url="https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": f"Bearer {auth_token}",
            },
            json={
                "model": "GigaChat",
                "messages": [{"role": "user", "content": message}],
                "temperature": 1,
                "top_p": 0.1,
                "n": 1,
                "stream": False,
                "max_tokens": 512,
                "repetition_penalty": 1,
                "update_interval": 0,
            },
        )
        data = response.json()
        try:
            return data["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            return "Не удалось получить ответ"
