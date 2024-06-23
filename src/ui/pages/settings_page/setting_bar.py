# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from typing import Union

import customtkinter as ctk
from customtkinter import CTkFont
from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu

from programtools.settings import Settings
from programtools.personalization import Color


class SettingBar(CTkFrame):
    """
    Класс панели с настройкой.
    """
    def __init__(self, master: Union[CTkFrame, tk.Tk, ctk.CTk],
                 title: str, option_menu_values: Union[list, tuple] = None,
                 command = None) -> None:
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - title (str): Название настройки.
        - option_menu_values ()
        """
        super().__init__(master=master,
                         height=40,
                         fg_color=Color('bar'),
                         corner_radius=7)

        # Шрифт для названия настройки.
        self.font = CTkFont('Roboto', size=20)

        # Создание и размещение текстового поля названия нацстройки.
        self.title_label = CTkLabel(self,
                                    height=40,
                                    text=title,
                                    anchor='w',
                                    font=self.font)
        self.title_label.pack(side=tk.LEFT, padx=5)

        # Создание переменной для опционального меню.
        option_menu_var = tk.Variable(value=Settings.get_value('theme'))
        # Создание и размещение опционального меню.
        self.option_menu = CTkOptionMenu(
            master=self,
            values=option_menu_values,
            command=command,
            variable=option_menu_var
        )
        self.option_menu.pack(side=tk.RIGHT, padx=5)

    def auto_place(self) -> None:
        """
        Размещает панель сверху.
        """
        self.pack(side=tk.TOP, padx=10, pady=(0, 10), anchor=tk.W, fill=tk.X)