import logging
from customtkinter import CTkImage
from PIL import Image, UnidentifiedImageError


logger = logging.getLogger(__name__)


BASE_PATH = "data\\icons\\left_menu\\"
ICONS = ["main", "home", "goals_and_objectives", "statistics", "settings"]


def get_icon_path(name, theme):
    return f"{BASE_PATH}{theme}\\{name}.png"


def get_icon(name) -> CTkImage:
    try:
        return CTkImage(
            light_image=Image.open(get_icon_path(name, 'light')),
            dark_image=Image.open(get_icon_path(name, 'dark')),
            size=(20, 20)
        )
    except (KeyError, UnidentifiedImageError, FileNotFoundError):
        logger.error(f"Unable to open image for icon {name}")
        placeholder = Image.new('RGBA', (20, 20), (0, 0, 0, 0))  # Создание прозрачного изображения размером 20x20
        return CTkImage(
            light_image=placeholder,
            dark_image=placeholder,
            size=(20, 20)
        )


MAIN = get_icon('main')
HOME = get_icon('home')
GOALS_AND_OBJECTIVES = get_icon('goals_and_objectives')
STATISTICS = get_icon('statistics')
SETTINGS = get_icon('settings')