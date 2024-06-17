# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from typing import Union

import customtkinter as ctk
from customtkinter import CTkFrame

from programtools.personalization import Color


class InnerFrame(CTkFrame):
    """
    Класс внутренней рамки.
    """
    def __init__(self, master: Union[ctk.CTk, tk.Tk, ctk.CTkFrame]):
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        """
        super().__init__(master, fg_color=Color('inner_frame'), corner_radius=7)

    def auto_place(self):
        """
        Размещает рамку с отступами от краёв в 10 пикселей.
        """
        self.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='nsew')