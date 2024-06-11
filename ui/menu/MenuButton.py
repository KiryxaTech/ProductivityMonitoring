from logging import getLogger
import tkinter as tk

from customtkinter import CTkButton
from customtkinter import CTkFont

from Ui import Colors
from Ui import Position
from Ui.Pages.Pages import Page


logger = getLogger(__name__)


class MenuButton(CTkButton):
    buttons: CTkButton = []
    linked_pages: Page = []

    def __init__(self, master, image, linked_page: Page, position = Position.TOP):
        font = CTkFont(
            'Segoe UI',
            size=13,
            weight='bold'
        )

        super().__init__(
            master,
            width=200,
            height=40,
            image=image,
            text='',
            font=font,
            fg_color=Colors.LEFT_BUTTON,
            corner_radius=7,
            anchor='w',
            command=self.show_linked_page
        )

        self.linked_page = linked_page
        self.name = linked_page.get_name()

        match position:
            case Position.TOP:
                self.top_place()
            case Position.BOTTOM:
                self.bottom_place()

        MenuButton.buttons.append(self)
        MenuButton.linked_pages.append(linked_page)

    def show_linked_page(self):
        logger.debug("Show page '%s'", self.name)
        for page in MenuButton.linked_pages:
            page.grid_forget()
        for button in MenuButton.buttons:
            button.configure(fg_color=Colors.LEFT_BUTTON)

        self.linked_page.auto_place()
        self.configure(fg_color=Colors.LEFT_BUTTON_ACTIVE)

    def top_place(self):
        self.pack(side=tk.TOP, pady=5, padx=5, anchor=tk.W, fill=tk.Y)

    def bottom_place(self):
        self.pack(side=tk.BOTTOM, pady=5, padx=5, anchor=tk.W, fill=tk.Y)

    def get_name(self):
        return self.name