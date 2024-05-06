import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

from utils import data

icons = data.get_settings()['left_menu_icons']

def get_icon(name) -> CTkImage:
    return CTkImage(
        light_image=Image.open(icons[name].replace('<theme>', 'light')),
        dark_image=Image.open(icons[name].replace('<theme>', 'dark')),
        size=(20, 20)
    )

MAIN = get_icon('main')
HOME = get_icon('home')
GOALS_AND_OBJECTIVES = get_icon('goals_and_objectives')
STATISTICS = get_icon('statistics')
SETTINGS = get_icon('settings')