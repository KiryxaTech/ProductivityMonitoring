# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk
from customtkinter import CTkButton
from customtkinter import CTkFont
from customtkinter import CTkFrame

from programtools.personalization import Color, Icon
from Ui.Menu.MenuButton import MenuButton
from Ui.OtherObjects import SeparateLine

# Создание логгера.
logger = getLogger(__name__)


class MainButton(CTkButton):
    """
    Класс главной кнопки в меню приложения.
    """
    is_menu_opened = False

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]) -> None:
        """
        Инициализация класса.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
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
            text='',
            font=font,
            image=Icon('main'),
            fg_color=Color('menu_button'),
            corner_radius=7,
            anchor='w',
            command=self.toggle_mode
        )

        self.master = master
        self.name = 'Menu'

    def auto_place(self) -> None:
        """
        Размещает главную кнопку вверху меню, размещает разделитьльную линию.
        """
        # Размещение главной кнопки вверху меню.
        self.pack(side=tk.TOP, pady=5, padx=5, anchor=tk.W, fill=tk.Y)
        
        SeparateLine(self, 200, 'Horizontal')

    def toggle_mode(self) -> None:
        """
        Открывает/Закрывает меню при клике на кнопку.
        """
        if MainButton.is_menu_opened:
            self.close_menu()
        else:
            self.open_menu()

    def open_menu(self) -> None:
        """
        Открывает меню.
        """
        logger.debug('Open menu')

        # Устанавливает текст для главной кнопки.
        self.configure(text=self.name)
        # Устанавливает текст для всез остальных кнопок меню.
        for button in MenuButton.buttons:
            button.configure(text=button.get_name())
        
        # Утсанавливает ширину меню в 180 пикселей.
        self.master.configure(width=180)

        # Свойство проверки режима меню в True.
        MainButton.is_menu_opened = True

    def close_menu(self) -> None:
        """
        Закрывает меню.
        """
        logger.debug('Close menu')
        # Убирает текст с кнопки.
        self.configure(text=None)
        # Убирает текст со всех остальных кнопок меню.
        for button in MenuButton.buttons:
            button.configure(text=None)

        # Утсанавливает ширину меню в 50 пикселей.
        self.master.configure(width=50)

        # Свойство проверки режима меню в False.
        MainButton.is_menu_opened = False