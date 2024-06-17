# Авторские права (c) KiryxaTechDev.

from logging import getLogger
from pathlib import Path
from typing import Union, Any

from programtools.static_meta import StaticMeta
from programtools.json_helper import JsonHelper


# Создание логгера.
logger = getLogger(__name__)


class Settings(metaclass=StaticMeta):
    """
    Класс, упрощающий работу с settings.json.
    """
    default_settings = {
        "theme": "System",
        "accent": "green",
        "icon_path": "data\\icons\\icon.ico"
    }
    settings_directory = Path(r'data\settings.json')

    def set_settings(settings: dict) -> None:
        """
        Изменяет настройки приложения.

        Параметры:
        - settings (dict): Словарь настроек.
        """
        logger.debug('Set settings.')
        JsonHelper.write(settings, Settings.settings_directory)

    def get_settings() -> dict:
        """
        Возращает настройки приложения.
        """
        settings = JsonHelper.read(Settings.settings_directory)

        if settings == {}:
            logger.debug("Create file %s", Settings.settings_directory)
            JsonHelper.write(Settings.default_settings, Settings.settings_directory)
            
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
            # Если str.
            return settings.get(key)
        elif isinstance(key, dict):
            # Если dict.
            result = {}
            for k in key:
                result[k] = settings.get(k)
            return result
        else:
            # Если передано не то значение.
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