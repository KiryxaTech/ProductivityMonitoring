import tkinter as tk

from customtkinter import CTkFrame
from customtkinter import CTkButton
from customtkinter import CTkFont

from Ui import Colors
from Ui.Menu import Icons
from Ui.Menu.MenuButton import MenuButton


class MainButton(CTkButton):
    is_menu_opened = False

    def __init__(self, master):
        font = CTkFont(
            'Segoe UI',
            size=13,
            weight='bold'
        )

        super().__init__(
            master,
            width=200,
            height=40,
            text='',
            font=font,
            image=Icons.MAIN,
            fg_color=Colors.LEFT_BUTTON,
            corner_radius=7,
            anchor='w',
            command=self.toggle_mode
        )

        self.master = master
        self.name = 'Menu'

        self.auto_place()

    def auto_place(self):
        self.pack(side=tk.TOP, pady=5, padx=5, anchor=tk.W, fill=tk.Y)
        self.separate_line = CTkFrame(
            master=self.master,
            width=200,
            height=2,
            fg_color=Colors.SEPARATE_LINE
        )
        self.separate_line.pack(side=tk.TOP, pady=1, padx=5)

    def toggle_mode(self):
        if MainButton.is_menu_opened:
            self.close_menu()
        else:
            self.open_menu()

    def open_menu(self):
        current_width = self.master.winfo_width()
        new_width = current_width + 2

        self.master.configure(width=new_width)

        if new_width >= 180:
            self.master.configure(width=180)
            MainButton.is_menu_opened = True

            self.configure(text=self.name)
            for button in MenuButton.buttons:
                button.configure(text=button.get_name())
            return

        self.after(10, self.open_menu)

    def close_menu(self):
        self.configure(text=None)
        for button in MenuButton.buttons:
            button.configure(text=None)

        self.master.configure(width=50)
        MainButton.is_menu_opened = False