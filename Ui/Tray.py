# Авторские права (c) KiryxaTechDev.

from pathlib import Path

from PIL import Image
from pystray import Icon, Menu, MenuItem as Item

from programtools.program import Program


# Константа икноки для трея.
ICON = Image.open(Path(r'data\icons\icon.ico'))


class Tray(Icon):
    """
    Класс трея программы.
    """
    def __init__(self):
        """
        Инициализирует класс.
        """
        super().__init__(
             name='ProductivityMonitoring',
             icon=ICON,
             menu=Menu(
                 Item('Exit', Program.exit)
             ),
             title='ProductivityMonitoring'
        )