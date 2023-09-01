'''App for managing data from a School'''


import tkinter as tk # Import the tkinter module
from tkinter import ttk # Import the ttk module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections, EntryFrame, button_frame # Import the Sections class from modules.py
from PIL import Image # Import the Image modules from PIL

#$------------------------ Functions
def get_data():
    '''Get data from the entry frames and save it in a variable'''
    global credentials
    credentials['user'] = user.entry.get()
    credentials['password'] = password.entry.get()
    return credentials

def show_password():
    '''Show the password'''
    if password.entry.cget('show') == '*':
        password.entry.configure(show='')
        password.button.configure(image=img['show'])
    else:
        password.entry.configure(show='*')
        password.button.configure(image=img['hide'])


#$------------------------ Create the Login window
App=ctk.CTk()
App.title('Nibble') # Set the title of the app
App.iconbitmap('Nibble/recursos/logo/Nibble.ico') # Set the icon of the app
App.after(50, lambda: App.state('zoomed')) # Maximize the app
App.minsize(900, 700) # Set the minimum size of the app


#$------------------------ Create the background image label of the app
img = ctk.CTkImage(Image.open('Nibble/recursos/background.jpg'), size=(1920,1080))
background = ctk.CTkLabel(App, image=img)
background.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # Place the background image label


#$------------------------ Create the login frames
# Create the login frame
login = Sections(App,720,615,50,'#eafbff','transparent',['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'])
login.pack(expand=True)

# Create the header frame
header = Sections(login, 680, 250, fcolor='transparent', bcolor='transparent')
header.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# Create the body frame
body = Sections(login, 620, 300, fcolor='transparent', bcolor='transparent')
body.place(relx=0.5, rely=0.7, anchor=tk.CENTER)


#$------------------------ c\Create the header widgets 
# Create the login icon
icon_selected = ctk.CTkImage(Image.open('Nibble/recursos/logo/Nibble-Logo-1.png'), size=(150,150))
icon_label = ctk.CTkLabel(header, image=icon_selected, corner_radius=50, text="")
icon_label.place(relx=0.23, rely=0.5, anchor=tk.CENTER)


# Create the login label
login_label = ctk.CTkLabel(header, text="Iniciar Sesión", font=('Arial', 50), bg_color='transparent', text_color='#243233')
login_label.place(relx=0.67, rely=0.5, anchor=tk.CENTER)


#$------------------------ Create the body widgets
# Create the user entry frame
user = EntryFrame(body, 450, 50,"Usuario      ")
user.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

# Password show/hide img
show = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-show.png'), size=(30,20))
hide = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-hide.png'), size=(30,20))
img = { 'show': show, 'hide': hide}

# Create the password entry frame
password = EntryFrame(body, 450, 50,"Contraseña", True, img['hide'], show_password)
password.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
password.entry.configure(show='*')

# Create the forgot credentials button
fg_credentials = button_frame(body, text='Olvide mis credenciales.', hover=False, txcolor='#47959b')
fg_credentials.place(relx=0.25, rely=0.56, anchor=tk.CENTER)

# Create the register button
registrarse_button = button_frame(body, 'Registrarse', None, True, 'transparent', '#47959b', 35, font=('Arial', 15))
registrarse_button.place(relx=0.3, rely=0.8, anchor=tk.CENTER)

# Create the login button
credentials = {"user": "", "password": ""} # Credentials dictionary
ingresar_button = button_frame(body, 'Ingresar', None, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
ingresar_button.place(relx=0.7, rely=0.8, anchor=tk.CENTER)

App.mainloop()
