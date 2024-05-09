import tkinter as tk
from customtkinter import CTkButton

from ui.pages.page import Page
from ui import colors


TOP = 0
BOTTOM = 1


class MenuButton(CTkButton):
    menu_is_opened = False
    width = 51
    buttons = []
    linked_pages: Page = []

    def __init__(self, master, image, linked_page: Page, position = TOP):
        MenuButton.buttons.append(self)
        MenuButton.linked_pages.append(linked_page)
        
        super().__init__(master,
                        width=40,
                        height=40,
                        image=image,
                        text='',
                        fg_color=colors.LEFT_BUTTON,
                        corner_radius=7,
                        command=self.show_linked_page
        )

        self.linked_page = linked_page

        if position == TOP:
            self.top_place()
        elif position == BOTTOM:
            self.bottom_place()

    def show_linked_page(self):
        if self.linked_page == None:
            if not MenuButton.menu_is_opened:
                self.open_menu()
            else:
                self.close_menu()
            return
        
        for page in MenuButton.linked_pages:
            if page == None: continue
            page.grid_forget()
        for button in MenuButton.buttons:
            button.configure(fg_color=colors.LEFT_BUTTON)

        self.linked_page.auto_place()
        self.configure(fg_color=colors.LEFT_BUTTON_ACTIVE)

    def top_place(self):
        self.pack(side=tk.TOP, pady=5, padx=5, anchor=tk.W, fill=tk.Y)

    def bottom_place(self):
        self.pack(side=tk.BOTTOM, pady=5, padx=5, anchor=tk.W, fill=tk.Y)

    def open_menu(self):
        current_width = self.master.winfo_width()
        new_width = current_width + 2

        self.master.configure(width=new_width)

        if new_width >= 203:
            self.master.configure(width=203)
            MenuButton.menu_is_opened = True
            return

        self.after(10, self.open_menu)


    def close_menu(self):
        current_width = self.master.winfo_width()
        print('cur:', current_width)
        new_width = current_width - 2
        print('new:', new_width)

        self.master.configure(width=new_width)

        if new_width <= 51:
            self.master.configure(width=51)
            MenuButton.menu_is_opened = False
            return

        self.after(10, self.close_menu)