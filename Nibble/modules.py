'''Modules of the app'''
import tkinter as ttk # Import the tkinter module
import customtkinter as ctk # Import the customtkinter module
from screeninfo import get_monitors # Import the get_monitors function from screeninfo

# todo Cambiar el valor de fcolor a transparent


#$ ------------------------ Classes
# Create the Frames for the app
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

# Create the entry frames for the app
class EntryFrame(ctk.CTkFrame):
    '''Entry frames of the app'''
    def __init__(self, parent, size_x, size_y, text, another = False, img = None, command = None):
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
            placeholder_text = text,
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

        self.label.grid(row=0, column=0, pady=5, padx=0, sticky='w')
        self.entry.grid(row=1, column=0, pady=5, padx=0 , sticky='w')


#$ ------------------------ Functions
# Create the button frames for the app
def button_frame(parent, text, command = None, hover = True, bcolor = 'transparent',fcolor = 'transparent', size_y = 28, txcolor = None, font = None):
    '''Button frames of the app'''
    button = ctk.CTkButton(
        master = parent,
        text = text,
        bg_color = bcolor,
        fg_color = fcolor,
        hover=hover,
        height= size_y,
        command = command,
        text_color=txcolor,
        font=font
        )
    return button

# Create the top level of the app
def top_level(parent ,size_x, size_y):
    '''Top level of the app'''
    top = ctk.CTkToplevel(master = parent)
    top.iconbitmap('Nibble/recursos/logo/Nibble.ico')
    top.title('Nibble')
    top.minsize(size_x, size_y)
    top.geometry(f'+{int(get_monitors()[0].width/2)-550}+{int(get_monitors()[0].height/2)-450}')
    parent.withdraw() # Hide the parent window

    # Create the close function
    def close():
        top.destroy()
        parent.deiconify()
        parent.after(50, lambda: parent.state('zoomed'))

    top.protocol("WM_DELETE_WINDOW", close) # Call the close function when the user close the window
    return top
