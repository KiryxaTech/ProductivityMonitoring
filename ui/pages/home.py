from .parent import ParentPage

PAGE_TITLE = 'Home'

class HomePage(ParentPage):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)