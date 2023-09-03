'''App for managing data from a School'''


import tkinter as tk # Import the tkinter module
from tkinter import ttk
from typing import Optional, Tuple, Union # Import the ttk module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections, EntryFrame, button_frame # Import the Sections class from modules.py
from PIL import Image # Import the Image modules from PIL


#$------------------------ Functions
def img_background(parent):
    '''Create the background image of the app'''
    img = ctk.CTkImage(Image.open('Nibble/recursos/background.jpg'), size=(1920,1080))
    img_label = ctk.CTkLabel(parent, image=img)
    img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    return img

#$------------------------ Classes
#^------------Login Layout
class Login(ctk.CTkFrame):
    '''Login Layout'''
    def __init__(self, parent):
        img_background(parent) # Create the background image label of the app
        super().__init__(
            master = parent,
            width=720,
            height=615,
            corner_radius=50,
            fg_color='#eafbff',
            bg_color='transparent',
            background_corner_colors=['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'],
        )

        #*----------------------------------------- frames
        # Create the header frame
        self.header = Sections(self, 680, 250, fcolor='transparent', bcolor='transparent')
        self.header.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        # Create the body frame
        self.body = Sections(self, 620, 300, fcolor='transparent', bcolor='transparent')
        self.body.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        #*----------------------------------------- header widgets
        # Create the login icon
        icon_selected = ctk.CTkImage(Image.open('Nibble/recursos/logo/Nibble-Logo-1.png'), size=(150,150))
        icon_label = ctk.CTkLabel(self.header, image=icon_selected, corner_radius=50, text="")
        icon_label.place(relx=0.23, rely=0.5, anchor=tk.CENTER)

        # Create the login label
        login_label = ctk.CTkLabel(self.header, text="Iniciar Sesión", font=('Arial', 50), bg_color='transparent', text_color='#243233')
        login_label.place(relx=0.67, rely=0.5, anchor=tk.CENTER)

        #*----------------------------------------- body widgets
        # Create the user entry frame
        self.user = EntryFrame(self.body, 450, 50,"Usuario      ")
        self.user.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        # Password show/hide img
        self.show = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-show.png'), size=(30,20))
        self.hide = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-hide.png'), size=(30,20))
        img = { 'show': self.show, 'hide': self.hide} # Create the dictionary

        # Create the password entry frame
        self.password = EntryFrame(self.body, 450, 50,"Contraseña", True, img['hide'], self.show_password)
        self.password.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        self.password.entry.configure(show='*') # Hide the password

        # Create the forgot credentials button
        fg_credentials = button_frame(self.body, text='Olvide mis credenciales.', hover=False, txcolor='#47959b')
        fg_credentials.place(relx=0.25, rely=0.56, anchor=tk.CENTER)

        #*----------------------------------------- footer widgets
        # Create the register button
        registrarse_button = button_frame(self.body, 'Registrarse', None, True, 'transparent', '#47959b', 35, font=('Arial', 15))
        registrarse_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

        # Create the login button
        self.credentials = {"user": "", "password": ""} # Credentials dictionary
        ingresar_button = button_frame(self.body, 'Ingresar', self.get_data, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        ingresar_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

    #*------------------------ Class Functions
    def show_password(self):
        '''Show the password'''
        if self.password.entry.cget('show') == '*':
            self.password.entry.configure(show='')
            self.password.button.configure(image=self.show)
        else:
            self.password.entry.configure(show='*')
            self.password.button.configure(image=self.hide)

    def get_data(self):
        '''Get data from the entry frames and save it in a variable'''
        self.credentials['user'] = self.user.entry.get()
        self.credentials['password'] = self.password.entry.get()


#$------------------------ Main App
App=ctk.CTk()
App.title('Nibble') # Set the title of the app
App.iconbitmap('Nibble/recursos/logo/Nibble.ico') # Set the icon of the app
App.after(50, lambda: App.state('zoomed')) # Maximize the app
App.minsize(900, 700) # Set the minimum size of the app

#*------------------------ Login
Login = Login(App)
Login.pack(expand=True)


#------------------------ Run the app
App.mainloop()
