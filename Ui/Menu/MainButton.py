# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk

from programtools.personalization import Color, Icon, Font
from Ui.Menu import Menu
from Ui.Menu.MenuButton import MenuButton
from Ui.OtherObjects import SeparateLine

# Создание логгера.
logger = getLogger(__name__)


class MainButton(MenuButton):
    """
    Класс главной кнопки в меню приложения.
    """
    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]) -> None:
        """
        Инициализация класса.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        """

        self.__name = 'Menu'
        self.__menu: 'Menu.Menu' = master

        # Инициализация кнопки со всеми настройками.
        super().__init__(master, Icon('main'), name=self.__name, command=self.__callback)

        MenuButton.buttons.append(self)

    def __callback(self):
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