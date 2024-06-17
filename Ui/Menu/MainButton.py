# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from logging import getLogger
from typing import Union

import customtkinter as ctk
from customtkinter import CTkButton
from customtkinter import CTkFont
from customtkinter import CTkFrame

from programtools.personalization import Color
from Ui.Menu import Icons
from Ui.Menu.MenuButton import MenuButton


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
            image=Icons.MAIN,
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
        
        # Создание и размещение разделительной линии.
        self.separate_line = CTkFrame(
            master=self.master,
            width=200,
            height=2,
            fg_color=Color('separate_line')
        )
        self.separate_line.pack(side=tk.TOP, pady=1, padx=5)

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
        # Получение текущей и новой ширины меню.
        current_width = self.master.winfo_width()
        new_width = current_width + 2

        # Применение новой ширины к меню.
        self.master.configure(width=new_width)

        if new_width >= 180:
            # Устанавливает ширину меню 180.
            self.master.configure(width=180)
            
            # Свойство проверки режима меню в True.
            MainButton.is_menu_opened = True

            # Устанавливает текст для главной кнопки.
            self.configure(text=self.name)
            # Устанавливает текст для всез остальных кнопок меню.
            for button in MenuButton.buttons:
                button.configure(text=button.get_name())
            logger.debug('Open menu')
            return

        # Вызывает метод через 10 мс.
        self.after(10, self.open_menu)

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