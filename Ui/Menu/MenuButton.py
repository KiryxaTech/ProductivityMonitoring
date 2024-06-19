# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union, Optional, Set

import customtkinter as ctk
from customtkinter import CTkButton

from programtools.personalization import Color, Icon, Font
from Ui import PositionConstants as PosConst
from Ui.Pages.Pages import Page


# Создание логгера.
logger = getLogger(__name__)


class MenuButton(CTkButton):
    """
    Класс MenuButton представляет собой кнопку в меню навигации.
    """
    buttons: Set['MenuButton'] = []

    def __init__(self,
                 master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame],
                 image: Union[ctk.CTkImage, Icon],
                 linked_page: Optional[Page] = None,
                 vertical_position: Union[PosConst.TOP, PosConst.BOTTOM] = PosConst.TOP,
                 **kwargs) -> None:
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - image (ctk.CTkImage): Изображение для кнопки.
        - linked_page (Page): Связанная с кнопкой страница.
        - vertical_position (Union[PosConst.TOP, PosConst.BOTTOM]): Позиция сверху или снизу меню.
        """

        self.kwargs = kwargs

        self.linked_page = linked_page
        self.name = str(self)

        self.__btn_callback = kwargs.pop('action', self.__callback)
        self.__font = Font('MenuButton')
        self.__fg_color = Color('menu_button')
        self.__hover_color = Color('menu_button_hover')
        self.__active_color = Color('menu_button_active')
        self.__text_color = Color('text')
        self.__vertical_position = vertical_position

        # Инициализация кнопки со всеми настройками.
        super().__init__(
            master,
            width=200,
            height=40,
            corner_radius=7,

            fg_color=self.__fg_color,
            hover_color=self.__hover_color,
            text_color=self.__text_color,

            text=None,
            font=self.__font,
            image=image,
            command=self.__btn_callback,
            anchor='w'
        )

        # Добавление кнопки в список кнопок меню.
        logger.debug(f"Button '{self.name}' added to buttons set.")
        MenuButton.buttons.append(self)

    def __str__(self):
        if self.linked_page is not None:
            return self.linked_page.get_name()
        return self.kwargs.pop('name', None)
    
    def show_linked_page(self) -> None:
        if self.linked_page is None:
            return
        
        Page.hide_pages()
        self.linked_page.auto_place()

    def vertical_position_pack(self):
        logger.debug(f"Button {self.name}")
        self.pack(side=self.__vertical_position, pady=5,
                  padx=5, anchor=tk.W, fill=tk.Y)
        
    def minimize(self):
        logger.debug(f"Button '{self.name}' minimized.")
        self.configure(text=None)

    def maximize(self):
        logger.debug(f"Button '{self.name}' maximized.")
        self.configure(text=self.name)

    @classmethod
    def minimize_buttons(cls):
        for btn in cls.buttons:
            btn.minimize()

    @classmethod
    def maximize_buttons(cls):
        for btn in cls.buttons:
            btn.maximize()

    def _change_default_color(self):
        logger.debug(f"Button '{self.name}' has its default color applied")
        self.configure(fg_color=self.__fg_color)

    def _change_active_color(self):
        logger.debug(f"Button '{self.name}' has its active color applied")
        self.configure(fg_color=self.__active_color)

    def __callback(self):
        logger.debug(f"Button '{self.name}' callback.")
        for btn in MenuButton.buttons:
            btn._change_default_color()

        self._change_active_color()
        self.show_linked_page()