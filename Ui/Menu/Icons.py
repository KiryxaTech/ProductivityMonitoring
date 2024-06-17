# Авторские права (c) KiryxaTechDev.
# Будет реализован класс Icon на основе этого модуля в programtools.personalization.
# Будет удалён после реализации класса Icon.

import logging
from pathlib import Path
from typing import Literal

from customtkinter import CTkImage
from PIL import Image, UnidentifiedImageError


logger = logging.getLogger(__name__)


BASE_PATH = "data\\icons\\left_menu\\"
ICONS = ["main", "home", "goals_and_objectives", "statistics", "settings"]


def get_icon_path(name: Literal['main', 'home', 'goals and objectives',
                                'statistics', 'settings'],
                  theme: Literal['Light', 'Dark']) -> Path:
    """
    Возвращает дирректорию иконки.

    Параметры:
    - name (Literal['main', 'home',
                    'goals and objectives',
                    'statistics', 'settings']): Имя иконки.
    - theme (Literal['Light', 'Dark']): Тема иконки.
    
    Возвращает:
    - 
    """
    path = f'{BASE_PATH}{theme}\\{name}.png'
    return Path(path)


def get_icon(name: Literal['main', 'home',
                            'goals and objectives',
                            'statistics', 'settings']) -> CTkImage:
    """
    Возвращает объект CtkImage.

    Параметры:
    - name (name: Literal['main', 'home',
                          'goals and objectives',
                          'statistics', 'settings']): Имя иконки.
    
    Возвращает:
    - CtkImage: Изображение для customtkinter.
    """
    try:
        # Создание изображения для светлой и тёмной темы.
        return CTkImage(
            light_image=Image.open(get_icon_path(name, 'light')),
            dark_image=Image.open(get_icon_path(name, 'dark')),
            size=(20, 20)
        )
    except (KeyError, UnidentifiedImageError, FileNotFoundError):
        logger.error(f"Unable to open image for icon {name}")
        # Создаём пустое изображение, если произошла ошибка.
        placeholder = Image.new('RGBA', (20, 20), (0, 0, 0, 0))
        return CTkImage(
            light_image=placeholder,
            dark_image=placeholder,
            size=(20, 20)
        )


# Константы иконкок.
MAIN = get_icon('main')
HOME = get_icon('home')
GOALS_AND_OBJECTIVES = get_icon('goals_and_objectives')
STATISTICS = get_icon('statistics')
SETTINGS = get_icon('settings')