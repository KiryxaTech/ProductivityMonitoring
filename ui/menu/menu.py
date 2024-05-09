import pywinstyles
import customtkinter as ctk
from customtkinter import CTkFrame

from utils import data
from ui.menu.menu_button import MenuButton
from ui import colors

class Menu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=51, corner_radius=0, fg_color=colors.LEFT_MENU, border_width=0)

        self.pack_propagate(False)

    def add_button_top(self, menu_button: MenuButton):
        menu_button.top_place()
        
    def add_button_bottom(self, menu_button: MenuButton):
        menu_button.bottom_place()

    def auto_place(self):
        self.grid(column=0, row=0, sticky='nsew')