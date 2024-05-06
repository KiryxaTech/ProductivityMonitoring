import tkinter as tk
from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu

class Bar(CTkFrame):
    def __init__(self, master, title, menu_values: list):
        super().__init__(master, height=75)

        setting_name = CTkLabel(self, height=75, text=title)
        setting_name.pack(side=tk.LEFT, padx=10)

        optional_menu = CTkOptionMenu(self, values=menu_values)
        optional_menu.pack(side=tk.RIGHT, padx=10)