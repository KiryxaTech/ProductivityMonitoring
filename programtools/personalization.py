# Авторские права (c) KiryxaTechDev.

from pathlib import Path
from logging import getLogger
from typing import Literal

import pywinstyles
import darkdetect
import customtkinter as ctk

from Ui import App
from programtools.static_meta import StaticMeta
from programtools.settings import Settings

# Создание логгера.
logger = getLogger(__name__)


class Color:
    """
    Класс цвета, который использует значения из конфигурационного файла.
    """

    # Константы для идентификации темы
    LIGHT = 'Light'
    DARK = 'Dark'
    LIGHT_ID = 0
    DARK_ID = 1

    def __init__(self, name: Literal['header', 'menu', 'menu_button', 
                                      'menu_button_active', 'page_bg', 
                                      'page_fg', 'dropdown_fg', 
                                      'inner_frame', 'separate_line', 
                                      'bar']):
        """
        Инициализирует экземпляр класса Color.

        :param name: Название цвета из предопределенного списка.
        :type name: Literal
        """
        self._name = name
        self._colors = self._load_colors_from_config()
        self._value = self._get_color(name)

    def __new__(cls, name):
        """
        Создает новый экземпляр класса Color и возвращает строковое значение цвета.

        :param name: Название цвета.
        :type name: str

        :return: Строковое представление цвета.
        :rtype: str
        """
        instance = super().__new__(cls)
        instance._colors = instance._load_colors_from_config()
        instance._value = instance._get_color(name)
        return instance._value

    @staticmethod
    def get_system_theme_id() -> int:
        """
        Получает идентификатор текущей темы системы.

        :return: Идентификатор темы системы.
        :rtype: int
        """
        return Color.LIGHT_ID if ctk.get_appearance_mode() == Color.LIGHT else Color.DARK_ID

    def _load_colors_from_config(self) -> dict:
        """
        Загружает цвета из конфигурационного файла.

        :return: Словарь с загруженными цветами.
        :rtype: dict
        """
        colors = {}
        try:
            with open(r'data\colors.config', 'r') as file:
                for line in file:
                    name, value = line.strip().split(': ')
                    colors[name] = value.split(', ')
                    logger.debug(f'Loaded color {name}: {colors[name]}')
        except Exception as e:
            logger.error(f'Error loading colors from config: {e}')

        return colors

    def _get_color(self, name: str):
        """
        Получает значение цвета по имени и текущей теме.

        :param name: Название цвета.
        :type name: str

        :return: Список значений цвета для разных тем или строку 'transparent'.
        """
        
        try:
            color_values = self._colors.get(name)
            
            if color_values is None:
                logger.error(f'Color {name} not found in config.')
                return 'transparent'
            
            # Возвращаем список значений, если цвет имеет значения для разных тем
            # Возвращаем строку 'transparent', если цветом является transparent
            if color_values == ['transparent']:
                return 'transparent'
            return color_values
        
        except Exception as e:
            logger.error(f'Error retrieving color {name}: {e}')
            return 'transparent'


class Personalization(metaclass=StaticMeta):
    """
    Класс персонализации.
    """
    themes = {
        'Light': {
            'theme': 'light',
            'accent_color': 'green',
            'header_color': Color('header')[0]
        },
        'Dark': {
            'theme': 'dark',
            'accent_color': 'dark-blue',
            'header_color': Color('header')[1]
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
        logger.debug(f"Theme update on '{theme}' (settings.json)")
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
        print(Color('header'))
        header = Color('header')[Color.get_system_theme_id()]
        
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

        # Установка темы.
        Personalization.set_theme(theme)

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
