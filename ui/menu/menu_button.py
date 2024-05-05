from customtkinter import CTkButton, CTkImage
from PIL import Image

from utils import data_utils

class MenuButton(CTkButton):
    count = 0

    def __init__(self, master, image, linked_page):
        super().__init__(master, width=40, height=40, image=image, text='', fg_color='transparent')

    def auto_place(self):
        self.place(x=10, y=10 + MenuButton.count * 50)
        
        MenuButton.count += 1