"""Модуль для загрузки конфигурации из переменных окружения с использованием dotenv."""

import os
from dotenv import load_dotenv


load_dotenv()


AUTH_KEY = os.getenv("AUTH_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
