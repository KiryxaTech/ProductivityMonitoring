from .parent import ParentPage

PAGE_TITLE = 'Statistics'

class StatisticsPage(ParentPage):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)