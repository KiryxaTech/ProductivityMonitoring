# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from typing import Union

import customtkinter as ctk
from customtkinter import CTkFont
from customtkinter import CTkFrame
from customtkinter import CTkLabel

from programtools.personalization import Color, Font
from Ui.Pages.Settings.InnerFrame import InnerFrame
from Ui.Pages.Settings.SettingBar import SettingBar

from programtools.personalization import Personalization


class Page(CTkFrame):
    """
    Главный класс для создания страниц.
    """
    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame], name: str):
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - name (str): Название страницы.
        """
        super().__init__(master, fg_color=Color('page_fg'), bg_color=Color('page_bg'), corner_radius=10)

        self.name = name

        # Создание и размещение заголовка страницы.
        self.title = CTkLabel(self, width=200, height=25, font=Font('PageTitle'), text=name, anchor='w')
        self.title.grid(column=0, row=0, padx=10, pady=5)

    def auto_place(self) -> None:
        """
        Размещает страницу справа от меню.
        """
        self.grid(column=1, row=0, sticky='nsew', padx=(0, 5), pady=(1, 5))

    def get_name(self) -> str:
        return self.name


class HomePage(Page):
    """
    Домашняя страница приложения.
    """
    def __init__(self, master):
        super().__init__(master, name='Home')


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

        # Создание весов для корректного размещения объектов.
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Создание и размещение внутренней рамки.
        inner_frame = InnerFrame(self)
        inner_frame.auto_place()

        # Создание и размещение панели настройки темы.
        theme_frame = SettingBar(inner_frame, 'Theme', ('System', 'Light', 'Dark'), command=Personalization.change_theme)
        theme_frame.auto_place()