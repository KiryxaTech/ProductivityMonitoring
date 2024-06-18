# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk
from customtkinter import CTkFrame

from programtools.personalization import Color


# Создание логгера.
logger = getLogger(__name__)

class Menu(CTkFrame):
    """
    Класс меню приложения
    """
    is_opened = False

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]) -> None:
        """
        Инициализирует класс.
        """
        super().__init__(master, width=51, corner_radius=0, fg_color=Color('menu'), border_width=0)

        # Разблокирует изменение размеров меню.
        self.pack_propagate(False)

    def __open(self):
        self.configure(width=180)

    def __close(self):
        self.configure(width=50)

    def switch(self) -> bool:
        match Menu.is_opened:
            case True:
                Menu.is_opened = False
                self.__close()
            case False:
                Menu.is_opened = True
                self.__open()

    def top_left_grid(self) -> None:
        """
        Размещает меню слева от основного интерфейса.
        """
        self.grid(column=0, row=0, sticky='nsew')