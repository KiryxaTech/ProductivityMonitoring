import pywinstyles
import customtkinter as ctk

from utils import data
from ui import colors

def set_theme(window, theme_id) -> None:
    settings = data.get_settings()

    if theme_id == colors.LIGHT_ID:
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')
        pywinstyles.change_header_color(window, colors.HEADER[colors.LIGHT_ID])

        settings['theme'] = colors.LIGHT

    elif theme_id in colors.DARK_ID:
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        pywinstyles.change_header_color(window, colors.HEADER[colors.DARK_ID])

        settings['theme'] = colors.LIGHT
    
    data.set_settings(settings)