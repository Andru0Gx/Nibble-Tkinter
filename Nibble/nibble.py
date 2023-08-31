'''App for managing data from a School'''


import tkinter as ttk # Import the tkinter module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections, EntryFrame, button_frame, top_level # Import the Sections class from modules.py
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

def open_app():
    '''Open the app window'''
    app = top_level(Login, 900, 700)
    get_data()
    print(credentials)


#$------------------------ Create the Login window
Login=ctk.CTk()
Login.title('Nibble') # Set the title of the app
Login.iconbitmap('Nibble/recursos/logo/Nibble.ico') # Set the icon of the app
Login.after(50, lambda: Login.state('zoomed')) # Maximize the app
Login.minsize(900, 700) # Set the minimum size of the app


#$------------------------ Create the background image label of the app
img = ctk.CTkImage(Image.open('Nibble/recursos/background.jpg'), size=(1920,1080))
background = ctk.CTkLabel(Login, image=img)
background.place(relx=0.5, rely=0.5, anchor=ttk.CENTER) # Place the background image label


#$------------------------ Create the login frames
# Create the login frame
login = Sections(Login,720,615,50,'#eafbff','transparent',['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'])
login.pack(expand=True)

# Create the header frame
header = Sections(login, 680, 250, fcolor='transparent', bcolor='transparent')
header.place(relx=0.5, rely=0.25, anchor=ttk.CENTER)

# Create the body frame
body = Sections(login, 620, 300, fcolor='transparent', bcolor='transparent')
body.place(relx=0.5, rely=0.7, anchor=ttk.CENTER)


#$------------------------ c\Create the header widgets 
# Create the login icon
icon_selected = ctk.CTkImage(Image.open('Nibble/recursos/logo/Nibble-Logo-1.png'), size=(150,150))
icon_label = ctk.CTkLabel(header, image=icon_selected, corner_radius=50, text="")
icon_label.place(relx=0.23, rely=0.5, anchor=ttk.CENTER)

# create the back icon
back_icon = ctk.CTkImage(Image.open('Nibble/recursos/icons/regresar.png'), size=(40,40))
back_button = ctk.CTkButton(
    header,text="" ,
    image=back_icon,
    bg_color='transparent',
    fg_color='transparent',
    hover=False,
    width=40,
    height=40,
    command=Login.destroy
    )
back_button.place(relx=0.05, rely=0.11, anchor=ttk.CENTER)

# Create the login label
login_label = ctk.CTkLabel(header, text="Iniciar Sesión", font=('Arial', 50), bg_color='transparent', text_color='#243233')
login_label.place(relx=0.67, rely=0.5, anchor=ttk.CENTER)


#$------------------------ Create the body widgets
# Create the user entry frame
user = EntryFrame(body, 450, 50,"Usuario      ")
user.place(relx=0.5, rely=0.15, anchor=ttk.CENTER)

# Password show/hide img
show = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-show.png'), size=(30,20))
hide = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-hide.png'), size=(30,20))
img = { 'show': show, 'hide': hide}

# Create the password entry frame
password = EntryFrame(body, 450, 50,"Contraseña", True, img['hide'], show_password)
password.place(relx=0.5, rely=0.4, anchor=ttk.CENTER)
password.entry.configure(show='*')

# Create the forgot credentials button
fg_credentials = button_frame(body, text='Olvide mis credenciales.', hover=False, txcolor='#47959b')
fg_credentials.place(relx=0.25, rely=0.56, anchor=ttk.CENTER)

# Create the register button
registrarse_button = button_frame(body, 'Registrarse', None, True, 'transparent', '#47959b', 35, font=('Arial', 15))
registrarse_button.place(relx=0.3, rely=0.8, anchor=ttk.CENTER)

# Create the login button
credentials = {"user": "", "password": ""} # Credentials dictionary
ingresar_button = button_frame(body, 'Ingresar', open_app, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
ingresar_button.place(relx=0.7, rely=0.8, anchor=ttk.CENTER)

Login.mainloop()
