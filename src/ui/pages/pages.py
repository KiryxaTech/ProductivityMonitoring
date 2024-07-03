# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from typing import Union, Set

import customtkinter as ctk
from customtkinter import CTkFrame

from programtools import Color, Personalization
from .page_title import PageTitle
from .settings_page import *
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
        theme_mode_bar = SettingBar(self.inner_frame, 'Theme mode', 'Color for application.')
        theme_mode_widget = OptionWidget(master=theme_mode_bar,
                                         values=('System', 'Light', 'Dark'),
                                         variable_value=Personalization.get_theme(),
                                         command=Personalization.set_theme)
        theme_mode_bar.add_widget(theme_mode_widget)

        accent_color_bar = SettingBar(self.inner_frame, 'Accent color', 'Accent color for application elements.')
        accent_color_widget = OptionWidget(master=accent_color_bar,
                                           values=('nebula', 'dark-blue', 'green'),
                                           variable_value=Personalization.get_accent(),
                                           command=Personalization.set_accent)
        accent_color_bar.add_widget(accent_color_widget)

        interface_scaling_bar = SettingBar(self.inner_frame, 'Interface scaling', 'Scaling widgets and text.')
        interface_scaling_widget = OptionWidget(master=interface_scaling_bar,
                                                values=('100%', '125%', '150%'),
                                                variable_value=Personalization.get_scaling(),
                                                command=Personalization.set_scaling)
        interface_scaling_bar.add_widget(interface_scaling_widget)

        transparency_mode_bar = SettingBar(self.inner_frame, 'Transparency (β)', 'Window transparency (Beta)')
        tranparency_mode_widget = SwitchWidget(transparency_mode_bar, Personalization.get_transparency(), Personalization.set_transparency)
        transparency_mode_bar.add_widget(tranparency_mode_widget)