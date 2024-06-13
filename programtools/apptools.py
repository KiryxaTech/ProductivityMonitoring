# Авторские права (c) KiryxaTechDev.
# Устаревший модуль. Создан для корректной работы приложения.
# В следущем коммите будет удалён.

import os
import json

from pathlib import Path
from typing import Literal, Union, Dict
from logging import getLogger

import darkdetect
import pywinstyles
import customtkinter as ctk

from Ui import App, Colors


logger = getLogger(__name__)


class StaticMeta(type):
    """
    Метакласс, который делает все методы внутри класса статическими.
    """
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                setattr(dct[attr_name], '__get__', lambda x: x)
        return super().__new__(cls, name, bases, dct)


from typing import Union, Dict, Any

class JsonHelper(metaclass=StaticMeta):
    def read(fp: Union[str, Path]) -> Dict[str, Any]:
        """
        Читает JSON-файл и возвращает словарь элементов.

        Параметры:
        - fp (Union[str, Path]): Путь до файла.

        Возвращает:
        - Dict[str, Any]: Словарь элементов.
        """
        try:
            logger.debug(f"Reading '{fp}'.")
            with open(fp, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"File {fp} not found. Returning an empty dictionary.")
            return {}

    def write(data: Dict[str, Any], fp: Union[str, Path]) -> None:
        """
        Записывает данные в JSON-файл.

        Параметры:
        - data (Dict[str, Any]): Данные для записи.
        - fp (Union[str, Path]): Путь до файла.
        """
        logger.debug(f"Writing '{fp}'.")
        with open(fp, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)


class Settings(metaclass=StaticMeta):
    default_settings = DEFAULT_SETTINGS = {
        "left_menu_icons": {
            "main": "data\\icons\\left_menu\\<theme>\\main.png",
            "home": "data\\icons\\left_menu\\<theme>\\home.png",
            "goals_and_objectives": "data\\icons\\left_menu\\<theme>\\goals_and_objectives.png",
            "statistics": "data\\icons\\left_menu\\<theme>\\statistics.png",
            "settings": "data\\icons\\left_menu\\<theme>\\settings.png"
        },
        "colors": {
            "header": [
                "#62d1d2",
                "#2a3441"
            ],
            "menu": [
                "#62d1d2",
                "#2a3441"
            ],
            "menu_button": "transparent",
            "menu_button_active": [
                "#0fbb71",
                "#445469"
            ],
            "separate_line": [
                "#62d1d2",
                "#2e2e2e"
            ],
            "page_background": [
                "#62d1d2",
                "#2a3441"
            ],
            "page_foreground": [
                "#f7f7f7",
                "#221f1f"
            ],
            "option_menu_dropdown_foreground": [
                "#62d1d2",
                "#2a3441"
            ],
            "settings_page_inner_frame": "transparent",
            "bar": [
                "#fbfbfb",
                "#2b2b2b"
            ]
        },
        "icon_path": "data\\icons\\icon.ico",
        "theme": "system",
        "language": "english",
        "region": "USA"
    }
    settings_path = Path(r'data\settings.json')

    def set_settings(settings: dict) -> None:
        """
        Изменяет настройки приложения.

        Параметры:
        - settings (dict): Словарь настроек.
        """
        logger.debug('Set settings.')
        JsonHelper.write(settings, Settings.settings_path)

    def get_settings() -> dict:
        """
        Возращает настройки приложения.
        """
        settings = JsonHelper.read(Settings.settings_path)

        if settings == {}:
            logger.debug("Create file %s", Settings.settings_path)
            JsonHelper.write(Settings.default_settings, Settings.settings_path)
            logger.debug('Return default settings')
            return Settings.default_settings
        
        logger.debug('Return settings.')
        return settings
    
    def get_value(key: Union[str, dict]) -> Any:
        """
        Возвращает значение по ключу.

        Параметры:
        - key (Union[str, dict]): Ключ или словарь с ключами.

        Возвращает:
        - Any: Значение, связанное с ключом.
        """
        settings = Settings.get_settings()

        if isinstance(key, str):
            return settings.get(key)
        elif isinstance(key, dict):
            result = {}
            for k in key:
                result[k] = settings.get(k)
            return result
        else:
            raise ValueError("Invalid key type. Expected str or dict.")
    
    def replace_value(key: str, new_value) -> None:
        """
        Заменяет значение по ключу.

        Параметры:
        - key (str): Ключ, по которому нужно заменить значение.
        - new_value (Any): Значение, на которое нужно заменить.
        """
        settings = Settings.get_settings()
        settings[key] = new_value
        Settings.set_settings(settings)


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


class Program(metaclass=StaticMeta):
    def exit() -> None:
        """
        Завершает все процессы приложения.
        """
        logger.debug('Program exit...')
        os._exit(0)