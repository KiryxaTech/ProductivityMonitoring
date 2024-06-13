from pathlib import Path
from logging import getLogger
from typing import Union, Any

from programtools.static_meta import StaticMeta
from programtools.json_helper import JsonHelper


# Создание логгера.
logger = getLogger(__name__)


class Settings(metaclass=StaticMeta):
    """
    Класс, упрощающий работу с settings.json.
    """
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