# Авторские права (c) KiryxaTechDev.

import os
from logging import getLogger

from .static_meta import StaticMeta


# Создание логгера.
logger = getLogger(__name__)


class Program(metaclass=StaticMeta):
    """
    Класс для управления программой.
    """
    def exit() -> None:
        """
        Завершает все процессы приложения.
        """
        logger.info('Exit the program.')
        # Завершение выполнения с кодом 0.
        os._exit(0)