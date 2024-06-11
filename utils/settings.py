from typing import Literal
from logging import getLogger

import darkdetect
import pywinstyles
import customtkinter as ctk

from utils import data
from Ui import App, Colors

logger = getLogger(__name__)

THEMES = {
    'Light': {
        'appearance_mode': 'light',
        'color_theme': 'green',
        'header_color': Colors.HEADER[Colors.LIGHT_ID]
    },
    'Dark': {
        'appearance_mode': 'dark',
        'color_theme': 'dark-blue',
        'header_color': Colors.HEADER[Colors.DARK_ID]
    }
}

def set_theme(theme: Literal['System', 'Light', 'Dark']) -> None:
    logger.debug('Get theme %s', theme)
    settings = data.get_settings()

    if theme == 'System':
        theme = darkdetect.theme()

    change_theme(theme)

def change_theme(theme: str):
    logger.debug("Set color theme '%s'", theme)
    ctk.set_appearance_mode(THEMES[theme]['appearance_mode'])
    ctk.set_default_color_theme(THEMES[theme]['color_theme'])
    logger.debug("Change header color '%s'", theme)
    pywinstyles.change_header_color(App, THEMES[theme]['header_color'])
