from .page import Page

PAGE_TITLE = 'Statistics'

class StatisticsPage(Page):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)