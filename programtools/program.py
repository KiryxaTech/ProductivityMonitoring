import os
from logging import getLogger

from programtools.static_meta import StaticMeta

# Создание логгера.
logger = getLogger(__name__)


class Program(metaclass=StaticMeta):
    """
    Класс для управления программой.
    """
    def start() -> None:
        """
        Запускает процессы приложения.
        """
        pass


    def exit() -> None:
        """
        Завершает все процессы приложения.
        """
        logger.info('Exit the program.')
        os._exit(0)