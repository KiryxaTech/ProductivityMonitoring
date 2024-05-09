from customtkinter import CTkFrame

from ui import colors
from ui.pages.page import Page
from ui.pages.settings_elements.inner_frame import InnerFrame
from ui.pages.settings_elements.setting_frame import SettingFrame
from utils import data

PAGE_TITLE = 'Settings'

class SettingsPage(Page):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)

        inner_frame = InnerFrame(self)
        inner_frame.auto_place()

        theme_frame = SettingFrame(inner_frame, 'Theme')
        theme_frame.auto_place()