import customtkinter as ctk
from utils import data

LIGHT = 'light'
DARK = 'dark'
LIGHT_ID = 0
DARK_ID = 1

def get_system_theme_id():
    return LIGHT_ID if ctk.get_appearance_mode().lower() == LIGHT else DARK_ID

colors = data.get_settings()['colors']
def get_color(name) -> list | str:
    return colors[name]

HEADER = get_color('header')
LEFT_MENU = get_color('menu')
LEFT_BUTTON = get_color('menu_button')
LEFT_BUTTON_ACTIVE = get_color('menu_button_active')
BG_PAGE = get_color('page_background')
FG_PAGE = get_color('page_foreground')
DROPDOWN_FG = get_color('option_menu_dropdown_foreground')
SETTINGS_PAGE_INNER_FRAME = get_color('settings_page_inner_frame')
SEPARATE_LINE = get_color('separate_line')
BAR = get_color('bar')