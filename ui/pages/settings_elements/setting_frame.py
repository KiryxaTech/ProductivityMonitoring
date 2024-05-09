import tkinter as tk

from customtkinter import CTkFrame, CTkLabel, CTkOptionMenu
from customtkinter import CTkFont


class SettingFrame(CTkFrame):
    count = 0

    def __init__(self, master, title):
        super().__init__(master, fg_color='#fff', height=100)

        self.font = CTkFont(
            'Segoe UI',
            size=20
        )
        self.title_label = CTkLabel(
            self,
            height=25,
            text=title,
            anchor='e',
            font=self.font
        )
        self.title_label.pack(side=tk.LEFT)

    def auto_place(self):
        self.grid(column=0, row=SettingFrame.count, padx=20, pady=10, sticky='nsew')
        self.configure(height=100)
        SettingFrame.count += 1