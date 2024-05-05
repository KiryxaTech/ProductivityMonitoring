import tkinter as tk
from customtkinter import CTkButton, CTkImage
from PIL import Image

from utils import data_utils

class MenuButton(CTkButton):

    def __init__(self, master, image, linked_page):
        super().__init__(master, width=50, height=40, image=image, text='', fg_color='transparent', corner_radius=0)

    def top_place(self):
        self.pack(side=tk.TOP)

    def bottom_place(self):
        self.pack(side=tk.BOTTOM)
