# GigaChatBot

Асинхронный Telegram-бот на Python с использованием **aiogram**, **GigaChat API**.  
Бот позволяет пользователям отправлять текстовые запросы и получать ответы от модели GigaChat.

---

## Функционал

- Генерация ответов с помощью GigaChat API.
- Асинхронная работа с Redis для хранения токена доступа.
- Состояния пользователя через **FSMContext** (например, "generating").
- Простая архитектура с модульной структурой проекта:
  - `app/handlers` — обработчики сообщений.
  - `app/gigachat` — работа с API GigaChat.
  - `app/connect_redis` — работа с Redis.

---

## Установка

1. Клонируйте репозиторий и перейдите в папку с проектом:
   ```bash
   git clone https://github.com/IgorKireev/gigachat-bot
   cd gigachatbot
   ```

2. Создайте .env файл на основе примера:
   ```bash
   .env.example
   ```
   
3. Для сборки и запуска контейнеров выполните команду:
   ```bash
   docker compose up --build
   ```