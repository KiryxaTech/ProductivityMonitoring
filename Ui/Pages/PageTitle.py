import tkinter as tk
from typing import Union

import customtkinter as ctk
from customtkinter import CTkLabel

from programtools import Font

class PageTitle(CTkLabel):
    """
    Заголовок для страницы.
    """

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame], title):
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - title (str): Текст заголовка страницы.
        """
        super().__init__(
            master,
            width=200,
            height=45,

            text=title,
            font=Font('PageTitle'),
            anchor='w'
        )