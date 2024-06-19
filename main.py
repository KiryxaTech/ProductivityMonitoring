# Авторские права (c) KiryxaTechDev.

from logging import getLogger, basicConfig, DEBUG
from threading import Thread

from Ui.App import App
from Ui.Tray import Tray


# Создание главного логгера программы.
logger = getLogger()
FORMAT = '[%(levelname)s] %(name)s | %(message)s'
basicConfig(level=DEBUG, format=FORMAT)


def main() -> None:
    """
    Главная функция приложения. Запускает все основные процессы.
    """
    logger.info('Start the program.')

    tray = Tray()
    tray_thr = Thread(target=tray.run)
    tray_thr.start()

    app = App()
    app.show_window()


if __name__ == '__main__':
    main()