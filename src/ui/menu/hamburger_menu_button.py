# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk

from . import *
from programtools import Icon
from ui.other_objects import SeparateLine

# Создание логгера.
logger = getLogger(__name__)


class HamburgerMenu(MenuButton):
    """
    Класс HamburgerButton представляет собой меню-гамбургер для открытия/закрытия меню навигации.
    """
    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]):
        """
        Инициализация класса.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        """

        self.name = 'Menu'
        self.__menu: 'NavigationMenu' = master

        # Инициализация меню-гамбурера.
        super().__init__(master, Icon('main'), name=self.name, action=self.__callback)

    def __callback(self):
        logger.debug(f"Button '{self.name}' callback.")
        self.__menu.switch()
        if self.__menu.is_opened:
            MenuButton.maximize_buttons()
        else:
            MenuButton.minimize_buttons()

    def vertical_position_pack(self) -> None:
        """
        Размещает главную кнопку вверху меню, размещает разделитьльную линию.
        """
        # Размещение главной кнопки вверху меню.
        self.pack(side=tk.TOP, pady=5, padx=5, anchor=tk.W, fill=tk.Y)
        SeparateLine(self, 200, 'horizontal')