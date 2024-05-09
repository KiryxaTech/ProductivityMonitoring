from customtkinter import CTkFrame

from Ui import Colors

class InnerFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=Colors.SETTINGS_PAGE_INNER_FRAME, corner_radius=7)

        self.columnconfigure(0, weight=1)
        #self.rowconfigure([0,1,2,3,4], weight=1)

    def auto_place(self):
        self.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky='nsew')