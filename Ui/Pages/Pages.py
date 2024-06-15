from customtkinter import CTkFrame
from customtkinter import CTkLabel
from customtkinter import CTkFont

from programtools.personalization import Color
from Ui.Pages.Settings.InnerFrame import InnerFrame
from Ui.Pages.Settings.SettingBar import SettingBar

from programtools.personalization import Personalization


class Page(CTkFrame):
    def __init__(self, master, name: str):
        super().__init__(master, fg_color=Color('page_fg'), bg_color=Color('page_bg'), corner_radius=10)

        self.name = name

        self.font = CTkFont('Segoe Ui', 20, 'bold')

        self.title = CTkLabel(self, width=200, height=25, font=self.font, text=name, anchor='w')
        self.title.grid(column=0, row=0, padx=10, pady=5)

    def auto_place(self):
        self.grid(column=1, row=0, sticky='nsew', padx=(0, 5), pady=(1, 5))

    def get_name(self) -> str:
        return self.name


class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, name='Home')


class GoalsAndObjectivesPage(Page):
    def __init__(self, master):
        super().__init__(master, name='Goals and objectives')


class StatisticsPage(Page):
    def __init__(self, master):
        super().__init__(master, name='Statistics')


class SettingsPage(Page):
    def __init__(self, master):
        super().__init__(master, name='Settings')

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        inner_frame = InnerFrame(self)
        inner_frame.auto_place()

        theme_frame = SettingBar(inner_frame, 'Theme', ('System', 'Light', 'Dark'), command=Personalization.change_theme)
        theme_frame.auto_place()