import json

import customtkinter as ctk
from customtkinter import CTk

from utils import data_utils
from ui import separator
from ui.separator import Separator
from ui.menu import icon
from ui.menu.menu import Menu
from ui.menu.menu_button import MenuButton
from ui.pages.home import HomePage


APP_NAME = 'ProductivityMonitoring'
APP_VERSION = '1.0'
APP_WIDTH = 1000
APP_HEIGHT = 500


class App(CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.settings = data_utils.read_json('data\\settings.json')

        # app settings
        self.title(APP_NAME)
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        self.minsize(400, 200)
        self.iconbitmap(self.settings['icon_path'])

        home_page = HomePage(self)
        home_page.auto_place()

        left_menu = Menu(self)

        menu_button = MenuButton(left_menu, icon.MENU, None)
        left_menu.add_button_top(menu_button)

        home_button = MenuButton(left_menu, icon.HOME, HomePage)
        left_menu.add_button_top(home_button)

        goals_and_objectives_button = MenuButton(left_menu, icon.GOALS_AND_OBJECTIVES, None)
        left_menu.add_button_top(goals_and_objectives_button)

        statistics_button = MenuButton(left_menu, icon.STATISTICS, None)
        left_menu.add_button_top(statistics_button)

        settings_button = MenuButton(left_menu, icon.SETTINGS, None)
        left_menu.add_button_bottom(settings_button)

        left_menu.auto_place()

        separator1 = Separator(self, separator.VERTICAL, 2000)
        separator1.place(x=50, y=0)

    def show_window(self):
        ctk.set_appearance_mode(self.settings['theme'])
        self.mainloop()