from customtkinter import CTkFrame

from ui.menu.menu_button import MenuButton

class Menu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=60, corner_radius=0, fg_color='#222222')

    def add_button(self, menu_button: MenuButton):
        menu_button.auto_place()

    def auto_place(self):
        self.grid(column=0, row=0, sticky='nsew')