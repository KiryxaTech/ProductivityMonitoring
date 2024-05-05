from ui.pages.home import HomePage
from ui.menu.menu import Menu
from ui.app import App
from ui.tray import Tray


def main():
    app = App()

    left_menu = Menu(app)
    left_menu.auto_place()

    home_page = HomePage(app)
    home_page.auto_place()

    app.show_window()

if __name__ == '__main__':
    main()