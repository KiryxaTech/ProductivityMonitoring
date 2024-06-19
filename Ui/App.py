# Авторские права (c) KiryxaTechDev.

from logging import getLogger

from customtkinter import CTk

from programtools import (Personalization, Color, Icon, Settings)
from Ui import PositionConstants as PosConst
from Ui.Menu import *
from Ui.Pages import *


# Создание логгера.
logger = getLogger(__name__)

# Константы для главного окна приложения.
APP_NAME = 'ProductivityMonitoring'
APP_VERSION = '1.0'
APP_WIDTH = 1100
APP_HEIGHT = 500
APP_MIN_WIDTH = 700
APP_MIN_HEIGHT = 400


class App(CTk):
    """
    Класс главного окна приложения.
    """
    def __init__(self) -> None: 
        """
        Инизиализирует класс.
        """
        super().__init__(fg_color=Color('page_bg'))

        Personalization.app_instance = self
        
        # Ставит тему приложения.
        Personalization.change_default_theme()
        # Минимальный размер окна для фиксации (pywinstyles уменьшает его до минимальных). 
        self.minsize(APP_WIDTH, APP_HEIGHT)

        # Добавляет весы размещения объектов.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Настройки окна.
        self.title(APP_NAME) # Название
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}') # Размеры
        self.iconbitmap(Settings.get_value('icon_path')) # Иконка
        self.minsize(APP_MIN_WIDTH, APP_MIN_HEIGHT) # Минимальный размер
        self.wm_geometry(f'+200+100') # Отступы от краёв экрана

        # Создание страниц приложения.
        home_page = HomePage(self)
        goals_objectives_page = GoalsAndObjectivesPage(self)
        statistics_page = StatisticsPage(self)
        settings_page = SettingsPage(self)

        home_page.auto_place()

        # Создание меню приложения.
        menu = NavigationMenu(self)
        menu.top_left_grid()

        # Создание кнопок в меню.
        main_button = HamburgerMenu(menu)
        main_button.vertical_position_pack()

        home_btn = MenuButton(
            menu,
            Icon('home'),
            home_page
        )
        home_btn.vertical_position_pack()
        
        goals_objectives_btn = MenuButton(
            menu,
            Icon('goals_and_objectives'),
            goals_objectives_page
        )
        goals_objectives_btn.vertical_position_pack()
        
        statistics_btn = MenuButton(
            menu,
            Icon('statistics'),
            statistics_page
        )
        statistics_btn.vertical_position_pack()
        
        settings_btn = MenuButton(
            menu,
            Icon('settings'),
            settings_page,
            PosConst.BOTTOM
        )
        settings_btn.vertical_position_pack()

    def show_window(self) -> None:
        """
        Показывает главное окно приложения.
        """
        try:
            logger.debug('Show window.')
            # Запуск главного цикла приложения.
            self.mainloop()
        except Exception as e:
            logger.error(f"Error running main loop: {e}")
        finally:
            logger.debug('Hide window.')
