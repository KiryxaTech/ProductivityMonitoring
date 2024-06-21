# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from typing import Union, Set

import customtkinter as ctk
from customtkinter import CTkFrame

from programtools import Color
from programtools import Personalization
from .page_title import PageTitle
from .settings_page import SettingBar
from .inner_frame import InnerFrame
from ui import position_constants as PosConst


class Page(CTkFrame):
    """
    Главный класс для создания страниц.
    """
    pages: Set['Page'] = []

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame], name: str, is_main: bool = False):
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - name (str): Название страницы.
        """
        super().__init__(master, fg_color=Color('page_fg'), bg_color=Color('page_bg'), corner_radius=7)

        self.name = name
        self.is_main = is_main

        self.title = PageTitle(self, name)
        self.title.pack(side=PosConst.TOP, padx=(10, 0), anchor=tk.W)
        
        self.inner_frame = InnerFrame(self)  # Создание экземпляра InnerFrame
        self.inner_frame.pack(side=PosConst.TOP, padx=0, pady=(0, 7), expand=True, fill=tk.BOTH)

        Page.pages.append(self)

        self._check_main()

    def show(self) -> None:
        """
        Размещает страницу справа от меню.
        """
        self.grid(column=1, row=0, sticky='nsew', padx=(0, 5), pady=(1, 5))

    def hide(self):
        """
        Скрывает страницу.
        """
        self.grid_forget()

    def get_name(self) -> str:
        return self.name
    
    @classmethod
    def hide_pages(cls):
        for page in cls.pages:
            page.hide()

    def _check_main(self):
        if self.is_main:
            self.show()


class HomePage(Page):
    """
    Домашняя страница приложения.
    """
    def __init__(self, master):
        super().__init__(master, name='Home', is_main=True)


class GoalsAndObjectivesPage(Page):
    """
    Страница задач и целей.
    """
    def __init__(self, master):
        super().__init__(master, name='Goals and objectives')


class StatisticsPage(Page):
    """
    Страница статистики.
    """
    def __init__(self, master):
        super().__init__(master, name='Statistics')


class SettingsPage(Page):
    """
    Страница параметров.
    """
    def __init__(self, master):
        super().__init__(master, name='Settings')

        # Создание и размещение панели настройки темы.
        theme_frame = SettingBar(self.inner_frame, 'Theme', ('System', 'Light', 'Dark'), command=Personalization.change_theme)
        theme_frame.auto_place()