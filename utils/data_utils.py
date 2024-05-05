import json

import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

def read_json(fp: str) -> dict:
    with open(fp, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def load_img(icon_path):
    return CTkImage(Image.open(icon_path.replace('<theme>', ctk.get_appearance_mode().lower())), size=(20, 20))