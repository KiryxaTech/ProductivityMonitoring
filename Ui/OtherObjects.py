# Авторские права (c) KiryxaTechDev.

from typing import Literal

from customtkinter import CTkFrame

from programtools.personalization import Color
from Ui import PositionConstants


class SeparateLine(CTkFrame):
    """
    Класс, представляющий собой разделительную линию.
    """
    def __init__(self, master, length: int, orientation: Literal['Vertical', 'Horizontal'], 
                 widht: int = 2) -> None:
        """
        Инициализирует класс.

        Параметры:
        - length (int): Длина линии.
        - orientation (Literal['Vertical', 'Horizontal']): Ориентация линии.
        - width (int): Ширина линии.
        """
        # Настройки в зависимости от положения.
        if orientation == PositionConstants.VERTICAL:
            height = 2
            widht = length
        elif orientation == PositionConstants.HORIZONTAL:
            height = length
            widht = 2
        else:
            raise ValueError(f"The value cannot be '{orientation}'. Available values: 'Vertical' or 'Horizontal'.")

        super().__init__(master, widht, height, fg_color=Color('separate_line'))