# Авторские права (c) KiryxaTechDev.

from logging import getLogger
from typing import Literal

import pywinstyles
import darkdetect
import customtkinter as ctk

from Ui import App, Colors
from programtools.static_meta import StaticMeta
from programtools.settings import Settings

# Создание логгера.
logger = getLogger(__name__)


class Personalization(metaclass=StaticMeta):
    """
    Класс персонализации.
    """
    themes = {
        'Light': {
            'theme': 'light',
            'accent_color': 'green',
            'header_color': Colors.HEADER[Colors.LIGHT_ID]
        },
        'Dark': {
            'theme': 'dark',
            'accent_color': 'dark-blue',
            'header_color': Colors.HEADER[Colors.DARK_ID]
        }
    }

    def set_theme(theme: Literal['System', 'Light', 'Dark']) -> None:
        """
        Применяет тему приложения.

        Параметры:
        - theme (Literal['System', 'Light', 'Dark']): Тема, которую нужно применить.
        """
        logger.debug(f"Get theme '{theme}'")

        # Записываем новую тему в настройки.
        Settings.replace_value('theme', theme)

        # Определяем тему системы для 'System'
        theme = Personalization.parse_theme(theme)

        # Изменяем тему.
        logger.debug(f"Change theme '{theme}'.")
        ctk.set_appearance_mode(theme)

    def get_theme() -> Literal['System', 'Light', 'Dark']:
        """
        Возвращает текущую тему приложения.

        Возвращает:
        - Literal['System', 'Light', 'Dark']: Текущая тема приложения.
        """
        return Settings.get_value('theme')

    def set_accent(accent: Literal['green', 'dark-blue']) -> None:
        """
        Применяет тему приложения.

        Параметры:
        - theme (Literal['System', 'Light', 'Dark']): Тема, которую нужно применить.
        """
        logger.debug(f"Get accent color '{accent}'")
        # Записываем новый акцентный цвет в настройки.
        Settings.replace_value('accent', accent)

        # Изменяем тему.
        logger.debug(f"Change theme '{accent}'.")
        ctk.set_default_color_theme(accent)

    def set_header(theme: Literal['System', 'Dark', 'Light']) -> None:
        """
        Применяет цвет заголовка окна в зависимости от темы.

        Параметры:
        - theme (Literal['System', 'Dark', 'Light']): Тема приложения.
        """
        logger.debug('Set the color of the header')

        # Определяем цвет заголовка для 'System'.
        theme = Personalization.parse_theme(theme)
        header = Settings.get_value('colors')['header'][0 if theme == 'Light' else 1]
        
        # Изменяем цвет заголовка.
        logger.debug(f"Change header '{theme}'.")
        pywinstyles.change_header_color(App, header)

    def change_theme(theme: Literal['System', 'Light', 'Dark']) -> None:
        """
        Применяет тему и акцентный цвет приложения.

        Параметры:
        - theme (Literal['System', 'Light', 'Dark']): Тема, которую нужно применить.
        """
        logger.debug("Set color theme '%s'", theme)

        theme = Personalization.parse_theme(theme)

        # Установка темы для приложения.
        if theme in Personalization.themes:
            Personalization.set_theme(theme)
        else:
            logger.warning("Theme '%s' not found in themes.", theme)

        # Установка акцентного цвета в зависитмости от темы.
        match theme:
            case 'System': accent = 'dark-blue' if Personalization.get_theme() == 'Light' else 'green'
            case 'Light': accent = 'dark-blue'
            case 'Dark': accent = 'green'
        Personalization.set_accent(accent)

        # Установка цвета для верхней панели приложения.
        Personalization.set_header(theme)

    def change_default_theme() -> None:
        """
        Применяет тему по умолчанию.
        """
        logger.debug('Changing default theme.')
        Personalization.change_theme(Personalization.get_theme())

    def parse_theme(theme: Literal['System', 'Light', 'Dark']) -> Literal['Light', 'Dark']:
        """
        Вычисляет тему.

        Параметры:
        - theme (Literal['System', 'Light', 'Dark']): Тема.

        Возвращает:
        - Literal['Light', 'Dark']: Реальную тему.
        """
        return darkdetect.theme() if theme == 'System' else theme
