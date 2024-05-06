import customtkinter as ctk
from utils import data

LIGHT = 'light'
DARK = 'dark'
LIGHT_ID = 0
DARK_ID = 1

def get_system_theme_id():
    return LIGHT_ID if ctk.get_appearance_mode().lower() == LIGHT else DARK_ID

colors = data.get_settings()['colors']
def get_color_list(name):
    color_list = [colors[LIGHT][name], colors[DARK][name]]
    if 'transparent' in color_list:
        return 'transparent'
    return color_list

HEADER = get_color_list('header')
LEFT_MENU = get_color_list('left_menu')
LEFT_BUTTON = get_color_list('left_button')
LEFT_BUTTON_ACTIVE = get_color_list('left_button_active')
BG_PAGE = get_color_list('bg_page')
FG_PAGE = get_color_list('fg_page')