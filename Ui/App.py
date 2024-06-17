# Авторские права (c) KiryxaTechDev.

from logging import getLogger

from customtkinter import CTk

from programtools.personalization import Personalization, Color, Icon
from programtools.settings import Settings
from Ui.Menu import MenuButton
from Ui.Menu.Menu import Menu
from Ui.Menu.MainButton import MainButton
from Ui.Menu.MenuButton import MenuButton
from Ui.Pages.Pages import *


# Создание логгера.
logger = getLogger(__name__)

# Константы для главного окна приложения.
APP_NAME = 'ProductivityMonitoring'
APP_VERSION = '1.0'
APP_WIDTH = 1100
APP_HEIGHT = 500
APP_MIN_WIDTH = 600
APP_MIN_HEIGHT = 350


class App(CTk):
    """
    Класс главного окна приложения.
    """
    def __init__(self) -> None: 
        """
        Инизиализирует класс.
        """
        super().__init__(fg_color=Color('page_bg'))
        
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
        goals_and_objectives_page = GoalsAndObjectivesPage(self)
        statistics_page = StatisticsPage(self)
        settings_page = SettingsPage(self)

        # Создание меню приложения.
        menu = Menu(self)
        menu.auto_place()

        # Создание кнопок в меню.
        main_button = MainButton(menu)
        main_button.auto_place()

        home_button = MenuButton(menu, Icon('home'), home_page)
        home_button.top_place()
        
        goals_and_objectives_button = MenuButton(menu, Icon('goals_and_objectives'), goals_and_objectives_page)
        goals_and_objectives_button.top_place()
        
        statistics_button = MenuButton(menu, Icon('statistics'), statistics_page)
        statistics_button.top_place()
        
        settings_button = MenuButton(menu, Icon('settings'), settings_page)
        settings_button.bottom_place()

        # Отображает домашнюю страницу.
        home_button.show_linked_page()

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
