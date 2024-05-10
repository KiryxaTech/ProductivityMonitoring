from customtkinter import CTkFrame

from Ui import Colors


class InnerFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Colors.LEFT_BUTTON, corner_radius=7)

        #self.pack_configure()

    def auto_place(self):
        self.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='nsew')