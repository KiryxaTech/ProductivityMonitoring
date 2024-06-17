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

    def add_button_top(self, menu_button: MenuButton) -> None:
        """
        Добавляет кнопку меню наверх меню.
        """
        logger.debug(f"Added '{menu_button.get_name()}' button on menu top side")
        menu_button.top_place()
        
    def add_button_bottom(self, menu_button: MenuButton) -> None:
        """
        Добавляет кноку меню вниз меню.
        """
        logger.debug(f"Added '{menu_button.get_name()}' button on menu bonntom side")
        menu_button.bottom_place()

    def auto_place(self) -> None:
        """
        Размещает меню слева от основного интерфейса.
        """
        self.grid(column=0, row=0, sticky='nsew')