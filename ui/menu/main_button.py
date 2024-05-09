from ui.menu.menu_button import MenuButton

class MainButton(MenuButton):
    def __init__(self, master):
        super().__init__(master, command=self.open_menu)

    def open_menu(self):
        self.master.configure(width=100)