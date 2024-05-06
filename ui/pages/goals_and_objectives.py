from .page import Page

PAGE_TITLE = 'Goals and objectives'

class GoalsAndObjectivesPage(Page):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)