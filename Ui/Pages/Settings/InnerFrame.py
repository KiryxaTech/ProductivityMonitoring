from customtkinter import CTkFrame

from programtools.personalization import Color


class InnerFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master,
                         fg_color=Color('inner_frame'),
                         corner_radius=7)

    def auto_place(self):
        self.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='nsew')