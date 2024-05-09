import darkdetect
import pywinstyles
import customtkinter as ctk

from utils import data
from Ui import app, colors

def set_theme(theme) -> None:
    settings = data.get_settings()

    theme = darkdetect.theme().lower() if theme == 'system' else theme.lower()

    if theme == colors.LIGHT:
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')
        pywinstyles.change_header_color(app, colors.HEADER[colors.LIGHT_ID])
        settings['theme'] = colors.LIGHT

    elif theme == colors.DARK:
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        pywinstyles.change_header_color(app, colors.HEADER[colors.DARK_ID])
        settings['theme'] = colors.DARK

    data.set_settings(settings)
