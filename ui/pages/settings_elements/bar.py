from utils import settings, data
import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu

from ui import colors

class Bar(CTkFrame):
    def __init__(self, master, title, menu_values: list):
        super().__init__(master, height=75)

        setting_name = CTkLabel(self, height=75, text=title)
        setting_name.pack(side=tk.LEFT, padx=10)

        optionmenu_var = tk.StringVar(value=data.get_settings()['theme'].capitalize())
        optional_menu = CTkOptionMenu(self,
                                      values=menu_values,
                                      variable=optionmenu_var,
                                      dropdown_fg_color=colors.DROPDOWN_FG,
                                      command=settings.set_theme
        )
        optional_menu.pack(side=tk.RIGHT, padx=10)