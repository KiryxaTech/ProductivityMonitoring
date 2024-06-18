# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk
from customtkinter import CTkFrame

from programtools.personalization import Color
from Ui.Menu.MenuButton import MenuButton


# Создание логгера.
logger = getLogger(__name__)

class Menu(CTkFrame):
    """
    Класс меню приложения
    """
    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]) -> None:
        """
        Инициализирует класс.
        """
        super().__init__(master, width=51, corner_radius=0, fg_color=Color('menu'), border_width=0)

        # Разблокирует изменение размеров меню.
        self.pack_propagate(False)

    def open(self):
        self.configure(width=180)

    def close(self):
        self.configure(width=50)

    def auto_place(self) -> None:
        """
        Размещает меню слева от основного интерфейса.
        """
        self.grid(column=0, row=0, sticky='nsew')