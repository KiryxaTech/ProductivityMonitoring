from typing import Literal
from logging import getLogger

import customtkinter as ctk

# Создание логгера.
logger = getLogger(__name__)

# Константы для идентификации темы.
LIGHT = 'Light'
DARK = 'Dark'
LIGHT_ID = 0
DARK_ID = 1

# Функция для получения текущего ID темы.
def get_system_theme_id():
    return LIGHT_ID if ctk.get_appearance_mode() == LIGHT else DARK_ID

# Функция для загрузки цветов из конфигурационного файла.
def load_colors_from_config(file_path):
    colors = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                name, value = line.strip().split(': ')
                colors[name] = value.split(', ')
                logger.debug(f'Loaded color {name}: {colors[name]}')
    except Exception as e:
        logger.error(f'Error loading colors from config: {e}')
    return colors

# Загрузка цветов при инициализации модуля.
colors = load_colors_from_config(r'data\colors.config')

# Функция для получения цвета по имени и текущей теме.
def get_color(name: Literal[
                  'header',
                  'menu',
                  'menu_button',
                  'menu_button_active',
                  'page_bg',
                  'page_fg',
                  'dropdown_fg',
                  'inner_frame',
                  'separate_line',
                  'bar']) -> str:
    theme_id = get_system_theme_id()
    color_value = colors.get(name)
    
    if color_value is None:
        logger.error(f'Color {name} not found in config.')
        return 'transparent'  # Возвращаем значение по умолчанию, если цвет не найден.
    
    if len(color_value) > theme_id:
        return color_value[theme_id]
    else:
        logger.error(f'Color list for {name} does not have enough elements.')
        return 'transparent'  # Возвращаем значение по умолчанию, если список слишком короткий.

# Константы для доступа к цветам.
HEADER = get_color('header')
LEFT_MENU = get_color('menu')
LEFT_BUTTON = get_color('menu_button')
LEFT_BUTTON_ACTIVE = get_color('menu_button_active')
BG_PAGE = get_color('page_bg')
FG_PAGE = get_color('page_fg')
DROPDOWN_FG = get_color('dropdown_fg')
SETTINGS_PAGE_INNER_FRAME = get_color('inner_frame')
SEPARATE_LINE = get_color('separate_line')
BAR = get_color('bar')

# Выводим текущий ID темы для отладки.
logger.debug(f'Current system theme id: {get_system_theme_id()}')