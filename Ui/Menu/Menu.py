from customtkinter import CTkFrame

from Ui import Colors
from Ui.Menu.MenuButton import MenuButton


class Menu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=51, corner_radius=0, fg_color=Colors.LEFT_MENU, border_width=0)

        self.pack_propagate(False)

    def add_button_top(self, MenuButton: MenuButton):
        MenuButton.top_place()
        
    def add_button_bottom(self, MenuButton: MenuButton):
        MenuButton.bottom_place()

    def auto_place(self):
        self.grid(column=0, row=0, sticky='nsew')