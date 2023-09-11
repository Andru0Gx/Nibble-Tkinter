'''Modules of the app'''
import tkinter as ttk # Import the tkinter module
import customtkinter as ctk # Import the customtkinter module


#$ ------------------------ Classes
# Create the Frames for the app
class Sections (ctk.CTkFrame):
    '''Frames of the app'''
    def __init__(self, parent, size_x, size_y, radius=0, fcolor="transparent", bcolor='transparent', bg_corner_colors=None, bdcolor = None, border_width = 0):
        super().__init__(
                master=parent,
                height=size_y,
                width=size_x,
                corner_radius=radius,
                fg_color=fcolor,
                bg_color=bcolor,
                background_corner_colors=bg_corner_colors,
                border_color=bdcolor,
                border_width=border_width,
            )

# Create the entry frames for the app
class EntryFrame(ctk.CTkFrame):
    '''Entry frames of the app'''
    def __init__(self, parent, size_x, size_y, text, another = False, img = None, command = None, layout = 1, placeholder = None):
        super().__init__( # Create the entry frame
                master = parent,
                width = size_x,
                height = size_y,
                bg_color='transparent',
                fg_color='transparent',
            )
        self.label = ctk.CTkLabel( # Create the label of the entry frame
            master = self,
            text = text,
            font = ('Arial', 20),
            bg_color = 'transparent',
            text_color='#243233',
            )
        self.entry = ctk.CTkEntry( # Create the entry of the entry frame
            master = self,
            width = size_x,
            font = ('Arial', 20),
            placeholder_text = placeholder,
            fg_color = '#f4fdff',
            bg_color = 'transparent',
            corner_radius = 10,
            border_color = '#243233',
            text_color='#243233',
            )
        if another: # If another is True, create the button of the entry frame
            self.button = ctk.CTkButton(
                master = self,
                text="",
                image = img,
                bg_color = 'transparent',
                fg_color = '#47959b',
                hover=True,
                height= 28,
                width= int (size_x/11),
                command = command,
                text_color='#243233',
                )
            self.entry.configure(width = int (size_x/1.13)) # Change the width of the entry
            self.button.grid(row=1, column=1, pady=5, padx=3, sticky='w') # Place the button

        if layout == 1: # If layout is 0, place the label and the entry in the frame
            self.label.grid(row=0, column=0, pady=5, padx=0, sticky='w')
            self.entry.grid(row=1, column=0, pady=5, padx=0 , sticky='w')
        elif layout == 2: # If layout is 1, place the label and the entry in the frame
            self.label.grid(row=0, column=0, pady=5, padx=10, sticky='w')
            self.entry.grid(row=0, column=1, pady=5, padx=10 , sticky='w')


#$ ------------------------ Functions
# Create the button frames for the app
def button_frame(parent, text, command = None, hover = True, bcolor = 'transparent',fcolor = 'transparent', size_y = 28,size_x = 140 ,txcolor = None, font = None, img = None):
    '''Button frames of the app'''
    button = ctk.CTkButton(
        master = parent,
        text = text,
        bg_color = bcolor,
        fg_color = fcolor,
        hover=hover,
        height= size_y,
        width= size_x,
        command = command,
        text_color=txcolor,
        font=font,
        image=img
        )
    return button
