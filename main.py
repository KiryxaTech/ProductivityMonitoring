from pywinstyles import get_accent_color
from logging import getLogger, basicConfig, DEBUG

from Ui.App import App
from Ui.tray import Tray

logger = getLogger()
FORMAT = '[%(levelname)s] %(name)s | %(message)s'
basicConfig(level=DEBUG, format=FORMAT)

def main():
    App()


if __name__ == '__main__':
    logger.info('Start program')
    main()
    logger.info('Stop program')