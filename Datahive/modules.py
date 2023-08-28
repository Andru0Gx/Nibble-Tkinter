'''Modules of the app'''
import customtkinter as ctk # Import the customtkinter module

class Sections (ctk.CTkFrame):
    '''Frames of the app'''
    def __init__(self, parent, size_x, size_y, radius=0, fcolor=None, bcolor='transparent', bg_corner_colors=None, bdcolor = None):
        super().__init__(
                master=parent,
                height=size_y,
                width=size_x,
                corner_radius=radius,
                fg_color=fcolor,
                bg_color=bcolor,
                background_corner_colors=bg_corner_colors,
                border_color=bdcolor
            )
