from customtkinter import CTkFrame

HORIZONTAL = 0
VERTICAL = 1

class Separator(CTkFrame):
    def __init__(self, master, orientation, line_size):

        if orientation == HORIZONTAL:
            width = line_size
            height = 2
        elif orientation == VERTICAL:
            width = 2
            height = line_size
        else:
            raise AttributeError(f"attribute '{orientation}' has not definied. Args: separator.HORISONTAL, separator.VERTICAL")

        super().__init__(master, width=width, height=height, corner_radius=0, fg_color='#505050')