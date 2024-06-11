from logging import getLogger
import json

import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

SETTINGS_FP = 'data\\settings.json'

logger = getLogger(__name__)

DEFAULT_SETTINGS = {
    "left_menu_icons": {
        "main": "data\\icons\\left_menu\\<theme>\\main.png",
        "home": "data\\icons\\left_menu\\<theme>\\home.png",
        "goals_and_objectives": "data\\icons\\left_menu\\<theme>\\goals_and_objectives.png",
        "statistics": "data\\icons\\left_menu\\<theme>\\statistics.png",
        "settings": "data\\icons\\left_menu\\<theme>\\settings.png"
    },
    "colors": {
        "header": [
            "#62d1d2",
            "#2a3441"
        ],
        "menu": [
            "#62d1d2",
            "#2a3441"
        ],
        "menu_button": "transparent",
        "menu_button_active": [
            "#0fbb71",
            "#445469"
        ],
        "separate_line": [
            "#62d1d2",
            "#2e2e2e"
        ],
        "page_background": [
            "#62d1d2",
            "#2a3441"
        ],
        "page_foreground": [
            "#f7f7f7",
            "#221f1f"
        ],
        "option_menu_dropdown_foreground": [
            "#62d1d2",
            "#2a3441"
        ],
        "settings_page_inner_frame": "transparent",
        "bar": [
            "#fbfbfb",
            "#2b2b2b"
        ]
    },
    "icon_path": "data\\icons\\icon.ico",
    "theme": "system",
    "language": "english",
    "region": "USA"
}

def read_json(fp: str) -> dict:
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error("File '%s' not found", fp)
        return {}

def write_json(data, fp):
    with open(fp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def set_settings(settings: dict):
    write_json(settings, SETTINGS_FP)

def get_settings():
    settings = read_json(SETTINGS_FP)
    if settings == {}:
        logger.debug("Create file %s", SETTINGS_FP)
        write_json(DEFAULT_SETTINGS, SETTINGS_FP)
        logger.debug('Return default settings')
        return DEFAULT_SETTINGS
    return settings