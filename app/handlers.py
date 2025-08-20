"""Модуль handler.py содержит обработчики сообщений для GigaChat бота на aiogram."""

from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from app.gigachat import communication
from app.gigachat import get_or_update_token


router = Router()


@router.message(CommandStart())
async def start_answer(message: Message):
    """
    Приветствует пользователя при старте бота.

    :param message: Объект сообщения от пользователя.
    :type message: Message
    :return: None
    :rtype: None
    """
    await message.answer(
        f"{message.from_user.full_name}, "
        f"Добро пожаловать в GigaChat Бот!\n"
        f"Введите ваш запрос: "
    )


@router.message(StateFilter("generating"))
async def wait_response(message: Message):
    """
    Сообщает пользователю, что ответ генерируется.
    Используется, когда пользователь находится в состоянии "generating".

    :param message: Объект сообщения от пользователя.
    :type message: Message
    :return: None
    :rtype: None
    """
    await message.answer("Ожидайте! Ответ генерируется...")


@router.message()
async def send_answer(message: Message, state: FSMContext):
    """
    Обрабатывает пользовательский запрос, отправляет его в GigaChat API и возвращает ответ.
    1. Устанавливает состояние "generating".
    2. Получает токен GigaChat через get_or_update_token().
    3. Отправляет сообщение в GigaChat API и получает ответ.
    4. Отправляет ответ пользователю.
    5. В случае ошибки сообщает об этом пользователю.
    6. Сбрасывает состояние после обработки.

    :param message: Объект сообщения от пользователя.
    :type message: Message
    :param state: Объект состояния пользователя для управления FSM.
    :type state: FSMContext
    :return: None
    :rtype: None
    """
    await state.set_state("generating")
    try:
        giga_token = await get_or_update_token()
        response = await communication(giga_token, message.text)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
    else:
        await message.answer(response)
    finally:
        await state.clear()
