from .parent import ParentPage

PAGE_TITLE = 'Settings'

class SettingsPage(ParentPage):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)