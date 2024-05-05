import json

import pywinstyles
import customtkinter as ctk
from customtkinter import CTk

from ui import colors

from ui.menu import icon
from ui.menu.menu import Menu
from ui.menu import menu_button
from ui.menu.menu_button import MenuButton

from ui.pages.home import HomePage
from ui.pages.goals_and_objectives import GoalsAndObjectivesPage
from ui.pages.statistics import StatisticsPage
from ui.pages.settings import SettingsPage

from utils import data_utils

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
        self.minsize(450, 250)
        self.iconbitmap(self.settings['icon_path'])

        home_page = HomePage(self)
        goals_and_objectives_page = GoalsAndObjectivesPage(self)
        statistics_page = StatisticsPage(self)
        settings_page = SettingsPage(self)

        left_menu = Menu(self)

        main_button = MenuButton(left_menu, icon.MAIN, None)
        home_button = MenuButton(left_menu, icon.HOME, home_page)
        goals_and_objectives_button = MenuButton(left_menu, icon.GOALS_AND_OBJECTIVES, goals_and_objectives_page)
        statistics_button = MenuButton(left_menu, icon.STATISTICS, statistics_page)
        settings_button = MenuButton(left_menu, icon.SETTINGS, settings_page, menu_button.BOTTOM)

        left_menu.auto_place()
        home_button.show_linked_page()

    def show_window(self):
        ctk.set_appearance_mode(self.settings['theme'])
        pywinstyles.change_header_color(self, colors.DARK_HEADER)
        self.mainloop()