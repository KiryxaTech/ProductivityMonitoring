from ui.pages.settings_elements.bar import Bar
from ui.pages.page import Page
from utils import data

PAGE_TITLE = 'Settings'

class SettingsPage(Page):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)

        theme_bar = Bar(self, 'Theme', ['System', 'Light', 'Dark'])
        theme_bar.place(x=10, y=10)