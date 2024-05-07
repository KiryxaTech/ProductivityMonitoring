import json

import pywinstyles
import customtkinter as ctk
from customtkinter import CTk

from ui import colors

from ui.menu import icons
from ui.menu.menu import Menu
from ui.menu import menu_button
from ui.menu.menu_button import MenuButton

from ui.pages.home import HomePage
from ui.pages.goals_and_objectives import GoalsAndObjectivesPage
from ui.pages.statistics import StatisticsPage
from ui.pages.settings import SettingsPage

from utils import data

APP_NAME = 'ProductivityMonitoring'
APP_VERSION = '1.0'
APP_WIDTH = 1000
APP_HEIGHT = 500
APP_MIN_WIDTH = 600
APP_MIN_HEIGHT = 350


class App(CTk):
    def __init__(self):
        super().__init__()
        self.settings = data.read_json('data\\settings.json')
        ctk.set_appearance_mode(self.settings['theme'])
        ctk.set_default_color_theme('green')

        #pywinstyles.apply_style(self, 'acrylic')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        # app settings
        self.title(APP_NAME)
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        self.minsize(APP_WIDTH, APP_HEIGHT)
        self.iconbitmap(self.settings['icon_path'])

        home_page = HomePage(self)
        goals_and_objectives_page = GoalsAndObjectivesPage(self)
        statistics_page = StatisticsPage(self)
        settings_page = SettingsPage(self)

        left_menu = Menu(self)

        main_button = MenuButton(left_menu, icons.MAIN, None)
        home_button = MenuButton(left_menu, icons.HOME, home_page)
        goals_and_objectives_button = MenuButton(left_menu, icons.GOALS_AND_OBJECTIVES, goals_and_objectives_page)
        statistics_button = MenuButton(left_menu, icons.STATISTICS, statistics_page)
        settings_button = MenuButton(left_menu, icons.SETTINGS, settings_page, menu_button.BOTTOM)

        left_menu.auto_place()
        home_button.show_linked_page()

    def show_window(self):
        pywinstyles.change_header_color(self, colors.HEADER[colors.get_system_theme_id()])

        self.minsize(APP_MIN_WIDTH, APP_MIN_HEIGHT)
        self.wm_geometry(f'+200+100')

        self.mainloop()