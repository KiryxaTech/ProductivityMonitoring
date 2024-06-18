# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union, List, Optional

import customtkinter as ctk
from customtkinter import CTkButton

from programtools.personalization import Color, Icon, Font
from Ui.Pages.Pages import Page
from Ui import PositionConstants as PosConst


# Создание логгера.
logger = getLogger(__name__)


class MenuButton(CTkButton):
    """
    Класс кнопки меню.
    """
    buttons: List['MenuButton'] = []

    def __init__(self,
                 master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame],
                 image: Union[ctk.CTkImage, Icon],
                 linked_page: Optional[Page] = None,
                 vertical_position: Union[PosConst.TOP, PosConst.BOTTOM] = PosConst.TOP,
                 **kwargs) -> None:
        """
        Инициализирует класс кнопки меню.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - image (ctk.CTkImage): Изображение для кнопки.
        - linked_page (Page): Связанная с кнопкой страница.
        """

        self.__btn_callback = kwargs.pop('command', self.__callback)
        self.__font = Font('MenuButton')
        self.__fg_color = Color('menu_button')
        self.__fg_color_active = Color('menu_button_active')

        # Инициализация кнопки со всеми настройками.
        super().__init__(
            master,
            width=200,
            height=40,
            image=image,
            text='',
            font=self.__font,
            fg_color=self.__fg_color,
            corner_radius=7,
            anchor='w',
            command=self.__btn_callback
        )

        self.linked_page = linked_page
        if linked_page is not None:
            self.name = linked_page.get_name()
        else:
            self.name = kwargs.pop('name', None)

        self.__vertical_position = vertical_position

        # Добавление кнопки в список кнопок меню.
        MenuButton.buttons.append(self)

    def __callback(self):
        for btn in MenuButton.buttons:
            btn._change_default_color()

        self._change_active_color()

        self.show_linked_page()

    def _change_default_color(self):
        self.configure(fg_color=self.__fg_color)

    def _change_active_color(self):
        self.configure(fg_color=self.__fg_color_active)

    def show_linked_page(self) -> None:
        if self.linked_page is None:
            return
        
        Page.hide_pages()
        self.linked_page.auto_place()

    def vertical_position_pack(self):
        self.pack(side=self.__vertical_position, pady=5,
                  padx=5, anchor=tk.W, fill=tk.Y)
        
    def minimize(self):
        self.configure(text=None)

    def maximize(self):
        self.configure(text=self.name)

    @classmethod
    def minimize_buttons(cls):
        for btn in cls.buttons:
            btn.minimize()

    @classmethod
    def maximize_buttons(cls):
        for btn in cls.buttons:
            btn.maximize()