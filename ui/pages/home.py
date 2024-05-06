import pywinstyles
import customtkinter as ctk
from customtkinter import CTkButton

from ui import colors
from ui.pages.page import Page
from utils import settings

PAGE_TITLE = 'Home'

class HomePage(Page):
    def __init__(self, master):
        super().__init__(master, title=PAGE_TITLE)