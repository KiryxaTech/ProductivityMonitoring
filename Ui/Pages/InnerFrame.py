# Авторские права (c) KiryxaTechDev.

import tkinter as tk

import customtkinter as ctk
from customtkinter import CTkFrame
from typing import Union

from programtools import Color


class InnerFrame(CTkFrame):
    """
    Внутренний фрейм страницы.
    """

    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]):
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        """
        super().__init__(master, fg_color=Color('inner_frame'), corner_radius=0)
        # Создание весов для корректного размещения объектов.
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)