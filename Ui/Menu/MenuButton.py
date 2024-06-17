# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk
from customtkinter import CTkButton
from customtkinter import CTkFont

from programtools.personalization import Color, Icon
from Ui.Pages.Pages import Page


# Создание логгера.
logger = getLogger(__name__)


class MenuButton(CTkButton):
    """
    Класс кнопки меню.
    """
    buttons: CTkButton = []
    linked_pages: Page = []

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame],
                 image: Union[ctk.CTkImage, Icon], linked_page: Page) -> None:
        """
        Инициализирует класс кнопки меню.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - image (ctk.CTkImage): Изображение для кнопки.
        - linked_page (Page): Связанная с кнопкой страница.
        """
        # Создание шрифта для кнопки.
        font = CTkFont(
            'Segoe UI',
            size=13,
            weight='bold'
        )

        # Инициализация кнопки со всеми настройками.
        super().__init__(
            master,
            width=200,
            height=40,
            image=image,
            text='',
            font=font,
            fg_color=Color('menu_button'),
            corner_radius=7,
            anchor='w',
            command=self.show_linked_page
        )

        self.linked_page = linked_page
        self.name = linked_page.get_name()

        # Добавление кнопки в список кнопок меню.
        MenuButton.buttons.append(self)
        # Добавление связанной страницы в список этих страниц.
        MenuButton.linked_pages.append(linked_page)

    def show_linked_page(self) -> None:
        """
        Показывает связанную страницу.
        """
        logger.debug("Show page '%s'", self.name)
        # Скрывает все другие страницы.
        for page in MenuButton.linked_pages:
            page.grid_forget()
        # Перекрашивание для обычной кнопки.
        for button in MenuButton.buttons:
            button.configure(fg_color=Color('menu_button'))

        # Размещение связанной страницы.
        self.linked_page.auto_place()
        # Перекрашивание для активной кнопки.
        self.configure(fg_color=Color('menu_button_active'))

    def top_place(self) -> None:
        """
        Размещает кнопку наверху меню.
        """
        self.pack(side=tk.TOP, pady=5, padx=5, anchor=tk.W, fill=tk.Y)

    def bottom_place(self) -> None:
        """
        Размещает кнопку внизу меню.
        """
        self.pack(side=tk.BOTTOM, pady=5, padx=5, anchor=tk.W, fill=tk.Y)

    def get_name(self) -> str:
        """
        Возвращает имя кнопки (связанной страницы).

        Возвращает:
        - str: Имя кнопки (связанной страницы).
        """
        return self.name