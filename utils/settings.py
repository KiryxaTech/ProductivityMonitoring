import darkdetect
import pywinstyles
import customtkinter as ctk

from utils import data
from Ui import App, Colors

def set_theme(theme) -> None:
    if type(theme) is not str:
        print(type(theme))
        return

    settings = data.get_settings()

    theme = theme.lower()
    if theme == 'system':
        theme = darkdetect.theme()
        print(theme)
    set_theme(settings)

    if theme == Colors.LIGHT:
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('green')
        pywinstyles.change_header_color(App, Colors.HEADER[Colors.LIGHT_ID])
    elif theme == Colors.DARK:
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')
        pywinstyles.change_header_color(App, Colors.HEADER[Colors.DARK_ID])