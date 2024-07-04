# Авторские права (c) KiryxaTechDev.

from logging import getLogger
from typing import Literal, List, Union
from pathlib import Path

import customtkinter as ctk
import darkdetect
import pywinstyles
from customtkinter import CTkImage, CTkFont
from PIL import Image
from JsonStructor import JsonFile

from .settings import Settings
from .static_meta import StaticMeta
from .json_helper import JsonHelper


# Создание логгера.
logger = getLogger(__name__)

# Константы для идентификации темы.
LIGHT_THEME = 'Light'
LIGHT_THEME_ID = 0
DARK_THEME = 'Dark'
DARK_THEME_ID = 1


class Color:
    """
    Класс цвета, который использует значения из конфигурационного файла.
    """
    colors_directory = Path(r'data\colors.json')
    colors_file = JsonFile(colors_directory)

    def __init__(self, name: Literal['header', 'menu', 'bar', 'menu_button',
                                     'menu_button_hover', 'menu_button_active',
                                     'page_bg', 'page_fg', 'dropdown_fg', 'text',
                                     'inner_frame', 'separate_line']) -> None:
        """
        Инициализирует экземпляр класса Color.

        Параметры:
        - name (Literal['header', 'menu', 'bar', 'menu_button',
                        'menu_button_hoover' 'menu_button_active',
                        'page_bg', 'page_fg', 'dropdown_fg', 'text',
                        'inner_frame', 'separate_line']): Название цвета из предопределенного списка.
        """
        self._name = name
        self._colors = Color.colors_file.get()
        self._value = self._get_color(name)

    def __new__(cls, name) -> Union[List[str], str]:
        """
        Создает новый экземпляр класса Color и возвращает строковое значение цвета.

        Парметры:
        - name (str): Название цвета.

        Возвращает:
        str: Строковое представление цвета.
        """
        # Создание нового экземпляра класса.
        instance = super().__new__(cls)

        instance._colors = Color.colors_file.get()
        instance._value = instance._get_color(name)

        return instance._value

    def _get_color(self, name) -> Union[List[str], str]:
        """
        Получает значение цвета по имени и текущей теме.

        Возвращает:
        - Union[List[str], str] Список значений цвета для разных тем или строку 'transparent'.
        """
        return self._colors.get(name)


class Icon(CTkImage):
    """
    Класс иконки для кнопки.
    """
    __icons_directory = Path(r'data\icons')

    def __init__(self, image_name: Literal['main', 'home', 'goals_and_objectives',
                                           'statistics', 'settings'], size: int = 25) -> None:
        """
        Инициализирует класс.

        Параметры:
        - image_name (Literal['main', 'home', 'goals and objectives',
                              'statistics', 'settings']): Имя иконки.
        - size (int): Размер иконки.
        """
        # Дирректории для светлой и тёмной темы иконки.
        light_icon_directory = f"{Icon.__icons_directory}\\menu\\Light\\{image_name}.png"
        dark_icon_directory = f"{Icon.__icons_directory}\\menu\\Dark\\{image_name}.png"

        # Иконки светлой и тёмной темы.
        light_icon = Image.open(light_icon_directory)
        dark_icon = Image.open(dark_icon_directory)

        super().__init__(light_image=light_icon,
                         dark_image=dark_icon,
                         size=(size, size))


class Font(CTkFont):
    """
    Класс шрифта.
    """
    def __init__(self, name: Literal['MenuButton', 'PageTitle', 'SettingBarTitle',
                                     'SettingBarDescription', 'SettingBarWidgetText']) -> None:
        """
        Инициализирует класс.

        Параметры:
        - name (Literal['MenuButton', 'PageTitle', 'SettingBarTitle', 'SettingBarDescription']): Имя шрифта.
        """
        font_list = JsonHelper.read(r'data\fonts.json').get(name)
        if len(font_list) == 2:
            family, size = font_list
            weight = None
        else:
            family, size, weight = JsonHelper.read(r'data\fonts.json').get(name)

        super().__init__(family, size, weight)


class Personalization(metaclass=StaticMeta):
    """
    Класс персонализации.
    """
    app_instance = None

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

    def set_accent(accent_name: Literal['Nebula']) -> None:
        """
        Применяет тему приложения.

        Параметры:
        - theme (Literal['Nebula']): Тема, которую нужно применить.
        """
        logger.debug(f"Get accent color '{accent_name}'")
        
        # Записываем новый акцентный цвет в настройки.
        Settings.replace_value('accent', accent_name)

        themes_directory = 'data\\themes'
        accent_name_path = f'{themes_directory}\\{accent_name}.json'

        try:
            ctk.set_default_color_theme(accent_name_path)
            logger.debug(f"Changed accent '{accent_name} ({accent_name_path})'.")
        except FileNotFoundError:
            logger.error(f'{accent_name} theme not found in {themes_directory}')

            ctk.set_default_color_theme('blue')
            logger.debug(f'Chanded default accent color')

    def get_accent() -> Literal['green', 'dark-blue', 'nebula']:
        return Settings.get_value('accent')

    def set_scaling(scaling: Literal['100%', '125%', '150%']):
        Settings.replace_value('scaling', scaling)

        scaling_factor = int(scaling.replace('%', '')) / 100
        ctk.set_widget_scaling(scaling_factor)

    def get_scaling():
        return Settings.get_value('scaling')

    def set_header(theme: Literal['System', 'Dark', 'Light']) -> None:
        """
        Применяет цвет заголовка окна в зависимости от темы.

        Параметры:
        - theme (Literal['System', 'Dark', 'Light']): Тема приложения.
        """
        logger.debug('Set the color of the header')

        header_color = Color('header')[Personalization.get_system_theme_id()]
        
        # Изменяем цвет заголовка.
        logger.debug(f"Change header '{header_color}'.")
        pywinstyles.change_header_color(Personalization.app_instance, header_color)

    def set_transparency() -> None:
        if Personalization.get_transparency() == "on": opacity = .75
        else: opacity = 1
        
        pywinstyles.set_opacity(Personalization.app_instance, opacity)
        Settings.replace_value('transparency', opacity)

    def get_transparency() -> float:
        return Settings.get_value('transparency')

    def change_default_theme() -> None:
        """
        Применяет тему по умолчанию.
        """
        logger.debug('Changing default theme.')
        Personalization.set_theme(Personalization.get_theme())
        Personalization.set_accent(Personalization.get_accent())
        Personalization.set_header(Personalization.get_theme())
        Personalization.set_scaling(Personalization.get_scaling())

    def parse_theme(theme: Literal['System', 'Light', 'Dark']) -> Literal['Light', 'Dark']:
        """
        Вычисляет тему.

        Параметры:
        - theme (Literal['System', 'Light', 'Dark']): Тема.

        Возвращает:
        - Literal['Light', 'Dark']: Реальную тему.
        """
        # Возвращает реальную тему.
        return darkdetect.theme() if theme == 'System' else theme
    
    def get_system_theme_id() -> int:
        """
        Получает идентификатор текущей темы системы.

        Возвращает:
        - str: Идентификатор темы системы.
        """
        if Personalization.get_theme() == LIGHT_THEME:
            return LIGHT_THEME_ID
        return DARK_THEME_ID
