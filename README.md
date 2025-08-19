# GigaChatBot

Асинхронный Telegram-бот на Python с использованием **aiogram**, **Redis** и **GigaChat API**.  
Бот позволяет пользователям отправлять текстовые запросы и получать ответы от модели GigaChat.

---

## 📦 Функционал

- Регистрация и обработка сообщений через Telegram Bot API.
- Генерация ответов с помощью GigaChat API.
- Асинхронная работа с Redis для хранения токена доступа.
- Состояния пользователя через **FSMContext** (например, "generating").
- Простая архитектура с модульной структурой проекта:
  - `app/handlers` — обработчики сообщений.
  - `app/gigachat` — работа с API GigaChat.
  - `app/connect_redis` — работа с Redis.
  - `config.py` — настройки проекта (токены, хосты, порты).

---

## ⚡ Установка

1. Клонируем репозиторий:

```bash
git clone https://github.com/yourusername/gigachatbot.git
cd gigachatbot
