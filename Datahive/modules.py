'''Modules of the app'''
import customtkinter as ctk # Import the customtkinter module

class Sections (ctk.CTkFrame):
    '''Frames of the app'''
    def __init__(self, parent, size_x, size_y):
        super().__init__(master = parent, height=size_y, width=size_x)
        