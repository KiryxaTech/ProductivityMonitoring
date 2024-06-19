# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk
from customtkinter import CTkFrame

from programtools.personalization import Color


# Создание логгера.
logger = getLogger(__name__)


class NavigationMenu(CTkFrame):
    """
    Класс NavigationMenu представляет собой меню навигации.
    """
    is_opened = False

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]):
        self.__fg_color = Color('menu')

        super().__init__(master, width=50, corner_radius=0, fg_color=self.__fg_color, border_width=0)

        # Разблокирует изменение размеров меню.
        self.pack_propagate(False)

    def __open(self):
        logger.debug('Opening the menu.')
        NavigationMenu.is_opened = True
        self.configure(width=180)

    def __close(self):
        logger.debug('Closing the menu.')
        NavigationMenu.is_opened = False
        self.configure(width=50)

    def switch(self) -> bool:
        if NavigationMenu.is_opened:
            self.__close()
        else:
            self.__open()

    def top_left_grid(self) -> None:
        self.grid(column=0, row=0, sticky='nsew')