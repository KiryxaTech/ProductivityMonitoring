from .parent import ParentPage

PAGE_TITLE = 'Goals and objectives'

class GoalsAndObjectivesPage(ParentPage):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)