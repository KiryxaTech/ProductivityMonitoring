import json

import customtkinter as ctk
from customtkinter import CTkImage
from PIL import Image

SETTINGS_FP = 'data\\settings.json'

def read_json(fp: str) -> dict:
    with open(fp, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_settings():
    with open(SETTINGS_FP, 'r', encoding='utf-8') as f:
        return json.load(f)

def set_settings(settings: dict):
    with open(SETTINGS_FP, 'w', encoding='utf-8') as f:
        json.dump(settings, f, indent=4)