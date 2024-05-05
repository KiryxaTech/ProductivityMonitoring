from customtkinter import CTkFrame

class Menu(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=60, corner_radius=0, fg_color='#222222')

    def auto_place(self):
        self.grid(column=0, row=0, sticky='nsew')