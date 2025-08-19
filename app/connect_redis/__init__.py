"""Пакет connect_redis содержит функции для работы с Redis."""

from .redis_client import set_value, get_value

__all__ = ["set_value", "get_value"]
