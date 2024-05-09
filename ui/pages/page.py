import pywinstyles
import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel
from customtkinter import CTkFont

from utils import data
from ui import colors

class Page(CTkFrame):
    def __init__(self, master, title: str):
        super().__init__(master, fg_color=colors.FG_PAGE, bg_color=colors.BG_PAGE, corner_radius=10)

        self.font = CTkFont('Segoe UI', 20, 'bold')

        self.title = CTkLabel(self, width=200, height=25, font=self.font, text=title, anchor='w')
        self.title.grid(column=0, row=0, padx=10, pady=5)

    def auto_place(self):
        self.grid(column=1, row=0, sticky='nsew')