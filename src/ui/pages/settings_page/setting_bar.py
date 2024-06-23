# Авторские права (c) KiryxaTechDev.

import tkinter as tk
from typing import Union, List, Tuple, Any

import customtkinter as ctk
from customtkinter import CTkFont
from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu

from programtools import Settings, Color, Font

class OptionWidget(CTkOptionMenu):
    def __init__(self,
                 master: Union[CTkFrame, tk.Tk, ctk.CTk],
                 values: Union[List, Tuple],
                 variable_value: Any,
                 command: Any):

        self._var = tk.Variable(value=variable_value)

        super().__init__(master=master,
                         values=values,
                         variable=self._var,
                         command=command)


class SettingBar(CTkFrame):
    """
    Класс панели с настройкой.
    """
    def __init__(self,
                 master: Union[CTkFrame, tk.Tk, ctk.CTk],
                 title: str,
                 description: str):
        """
        Инициализирует класс.

        Параметры:
        - master (Union[ctk.CTk, tk.Tk, ctk.CTkFrame]): Объект, на который будет помещен экземпляр.
        - title (str): Название настройки.
        - option_menu_values ()
        """
        super().__init__(master=master,
                         height=100,
                         fg_color=Color('bar'),
                         corner_radius=7,
                         border_color='#aaaaaa',
                         border_width=2)

        title_frame = CTkFrame(self,
                               height=50,
                               fg_color='transparent',
                               border_width=0)
        title_frame.pack(side=tk.LEFT, padx=5, pady=2)

        # Создание и размещение текстового поля названия настройки.
        bar_title = CTkLabel(title_frame,
                            height=20,
                            text=title,
                            anchor='s',
                            font=Font('SettingBarTitle'))
        bar_title.place(x=5, y=5)

        bar_description = CTkLabel(title_frame,
                                   height=15,
                                   text=description,
                                   text_color='#999999',
                                   anchor='s',
                                   font=Font('SettingBarDescription'))
        bar_description.place(x=5, y=30)
    
    def add_widget(self, widget: Union[OptionWidget]):
        widget.pack(side=tk.RIGHT, padx=5)

    def auto_place(self) -> None:
        """
        Размещает панель сверху.
        """
        self.pack(side=tk.TOP, padx=10, pady=(0, 10), anchor=tk.W, fill=tk.X)