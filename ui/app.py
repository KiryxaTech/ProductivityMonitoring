import json

import customtkinter as ctk
from customtkinter import CTk

import utils.data_utils as data_utils


APP_NAME = 'ProductivityMonitoring'
APP_VERSION = '1.0'
APP_WIDTH = 1000
APP_HEIGHT = 500


class App(CTk):
    def __init__(self):
        super().__init__()

        self.settings = data_utils.read_json('data\\settings.json')

        # app settings
        self.title = APP_NAME
        self.geometry(f'{APP_WIDTH}x{APP_HEIGHT}')
        self.iconbitmap(self.settings['icon_path'])

    def show_window(self):
        ctk.set_appearance_mode(self.settings['theme'])
        self.mainloop()