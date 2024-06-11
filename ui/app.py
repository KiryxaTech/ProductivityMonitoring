from logging import getLogger
import tkinter as tk

import pywinstyles
import customtkinter as ctk
from customtkinter import CTk

from Ui import Colors
from Ui import Position

from Ui.Menu import Icons
from Ui.Menu import MenuButton
from Ui.Menu.Menu import Menu
from Ui.Menu.MainButton import MainButton
from Ui.Menu.MenuButton import MenuButton

from Ui.Pages.Pages import *

from utils import data

logger = getLogger(__name__)

APP_NAME = 'ProductivityMonitoring'
APP_VERSION = '1.0'
APP_WIDTH = 1100
APP_HEIGHT = 500
APP_MIN_WIDTH = 600
APP_MIN_HEIGHT = 350


class App(CTk):
    def __init__(self):        
        super().__init__(fg_color=Colors.BG_PAGE)
        self.settings = data.read_json('data\\settings.json')
        ctk.set_appearance_mode(self.settings['theme'])
        ctk.set_default_color_theme('green')

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

        main_button = MainButton(left_menu)
        home_button = MenuButton(left_menu, Icons.HOME, home_page)
        goals_and_objectives_button = MenuButton(left_menu, Icons.GOALS_AND_OBJECTIVES, goals_and_objectives_page)
        statistics_button = MenuButton(left_menu, Icons.STATISTICS, statistics_page)
        settings_button = MenuButton(left_menu, Icons.SETTINGS, settings_page, Position.BOTTOM)

        left_menu.auto_place()
        home_button.show_linked_page()

        self.show_window()


    def show_window(self):
        pywinstyles.change_header_color(self, Colors.HEADER[Colors.get_system_theme_id()])

        self.minsize(APP_MIN_WIDTH, APP_MIN_HEIGHT)
        self.wm_geometry(f'+200+100')

        logger.debug('Show window')
        self.mainloop()
        logger.debug('Hide window')