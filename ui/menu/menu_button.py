import tkinter as tk
from customtkinter import CTkButton

from ui.pages.parent import ParentPage
from ui import colors


TOP = 0
BOTTOM = 1


class MenuButton(CTkButton):
    buttons = []
    linked_pages: ParentPage = []

    def __init__(self, master, image, linked_page: ParentPage, position = TOP):
        MenuButton.buttons.append(self)
        MenuButton.linked_pages.append(linked_page)
        
        super().__init__(master,
                         width=40,
                         height=40,
                         image=image,
                         text='',
                         fg_color=colors.DARK_LEFT_BUTTON,
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
            self.master.configure(width=100)
            return
        
        for page in MenuButton.linked_pages:
            if page == None: continue
            page.grid_forget()
        for button in MenuButton.buttons:
            button.configure(fg_color=colors.DARK_LEFT_BUTTON)

        self.linked_page.auto_place()
        self.configure(fg_color=colors.DARK_LEFT_BUTTON_ACTIVE)

    def top_place(self):
        self.pack(side=tk.TOP, pady=5, padx=5)

    def bottom_place(self):
        self.pack(side=tk.BOTTOM, pady=5, padx=5)
