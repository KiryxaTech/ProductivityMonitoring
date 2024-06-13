import os

from pathlib import Path

from PIL import Image
from pystray import Icon, Menu, MenuItem as Item

from programtools.program import Program

ICON = Image.open(Path(r'data\icons\icon.ico'))


class Tray(Icon):
    def __init__(self):
        super().__init__(
             name='ProductivityMonitoring',
             icon=ICON,
             menu=Menu(
                 Item('Exit', Program.exit)
             ),
             title='ProductivityMonitoring'
        )