from pywinstyles import get_accent_color

from Ui.App import App
from Ui.Tray import Tray

def main():
    print(get_accent_color())
    
    app = App()
    app.show_window()


if __name__ == '__main__':
    main()