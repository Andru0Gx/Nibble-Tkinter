'''App for managing data from a School'''


import tkinter as tk # Import the tkinter module
from tkinter import ttk
from tkinter import messagebox # Import the messagebox module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections, EntryFrame, button_frame # Import the Sections class from modules.py
from PIL import Image # Import the Image modules from PIL

#todo - Sidebar con un .pack y cuando se pase el mouse se aumente el tamaño horizontalmente, los labels ya estaran creados

#$------------------------ Functions
#^------------Loginto the app
def loginto_app(credentials: dict):
    '''Check if the credentials are correct'''
    if credentials['user'] == Login_window.user.entry.get() and credentials['password'] == Login_window.password.entry.get():
        img_label.destroy()
        Login_window.destroy()
        background.configure(width=1920, height=1080, corner_radius=0)
    else:
        messagebox.showerror('Error', 'Usuario o contraseña incorrectos')

#^------------Loginto Register
def loginto_register(parent):
    '''Change the layout to register'''
    parent.destroy()
    RegisterLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#^------------Back to login
def back_to_login(parent):
    '''Change the layout to login'''
    parent.destroy()
    LoginLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)




#$------------------------ Classes
#^------------Login Layout
class LoginLayout(ctk.CTkFrame):
    '''Login Layout'''
    def __init__(self, parent):
        super().__init__(
            master = parent,
            width=720,
            height=615,
            corner_radius=50,
            fg_color='transparent',
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
        login_label = ctk.CTkLabel(self.header, text="Iniciar Sesión", font=('Arial', 50, "bold"), bg_color='transparent', text_color='#243233')
        login_label.place(relx=0.67, rely=0.5, anchor=tk.CENTER)

        #*----------------------------------------- body widgets
        # Create the user entry frame
        self.user = EntryFrame(self.body, 450, 50,"Usuario      ")
        self.user.grid(row=0, column=0, pady=0, padx=20, sticky='e')

        # Password show/hide img
        self.show = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-show.png'), size=(30,20))
        self.hide = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-hide.png'), size=(30,20))
        pass_img = { 'show': self.show, 'hide': self.hide} # Create the dictionary

        # Create the password entry frame
        self.password = EntryFrame(self.body, 450, 50,"Contraseña", True, pass_img['hide'], self.show_password)
        self.password.grid(row=1, column=0, pady=0, padx=20 , sticky='e')
        self.password.entry.configure(show='*') # Hide the password

        # Create the forgot credentials button
        fg_credentials = button_frame(self.body, text='Olvide mis credenciales.', hover=False, txcolor='#47959b')
        fg_credentials.grid(row=2, column=0, pady=0, padx=20 , sticky='w')

        #*----------------------------------------- footer widgets
        # Create the register button
        registrarse_button = button_frame(self.body, 'Registrarse', lambda: loginto_register(self), True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        registrarse_button.grid(row=3, column=0, pady=25, padx=20 , sticky='w')

        # Create the login button
        self.credentials = {"user": "admin", "password": "1234"} # Credentials dictionary
        ingresar_button = button_frame(self.body, 'Ingresar', lambda:loginto_app(self.credentials), True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        ingresar_button.grid(row=3, column=0, pady=0, padx=20 , sticky='e')

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


#^------------Register Layout
class RegisterLayout(ctk.CTkFrame):
    '''Register Layout'''
    def __init__(self, parent):
        super().__init__(
            master = parent,
            width=720,
            height=615,
            corner_radius=50,
            fg_color='transparent',
            bg_color='transparent',
            background_corner_colors=['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'],
        )

        #*----------------------------------------- frames
        # Create the header frame
        self.header = Sections(self, 680, 100, fcolor='transparent', bcolor='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = Sections(self, 680, 400, fcolor='transparent', bcolor='transparent')
        self.body.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        # Create the footer frame
        self.footer = Sections(self, 680, 80, fcolor='transparent', bcolor='transparent')
        self.footer.place(relx=0.5, rely=0.92, anchor=tk.S)


        #*----------------------------------------- header widgets
        # Create the back button
        back_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/back.png'), size=(30,30))
        back_button = button_frame(self.header,"", lambda: back_to_login(self),True,'transparent','transparent',30,30,img= back_img)
        back_button.place(relx=0.05, rely=0.5, anchor=tk.CENTER)

        # Create the register label
        tittle_label = ctk.CTkLabel(self.header, text="Registrarse", font=('Arial', 30, "bold"), bg_color='transparent', text_color='#000000')
        tittle_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #*----------------------------------------- body widgets
        # Create the user entry frame
        self.user = EntryFrame(self.body, 275, 50,"Usuario      ")
        self.user.grid(row=0, column=0, pady=5, padx=20, sticky='e')

        # Create the email entry frame
        self.email = EntryFrame(self.body, 275, 50,"Correo electronico")
        self.email.grid(row=1, column=0, pady=5, padx=20 , sticky='e')

        # Create the password entry frame
        self.password = EntryFrame(self.body, 275, 50,"Contraseña", False)
        self.password.grid(row=2, column=0, pady=5, padx=20 , sticky='e')

        # Create the confirm password entry frame
        self.confirm_password = EntryFrame(self.body, 275, 50,"Confirmar contraseña", False)
        self.confirm_password.grid(row=3, column=0, pady=5, padx=20 , sticky='e')


        # Create security question entry frame
        self.security_question = EntryFrame(self.body, 275, 50,"Cual es tu color favorito?")
        self.security_question.grid(row=0, column=1, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_answer = EntryFrame(self.body, 275, 50,"Cual es tu deporte favorito?")
        self.security_answer.grid(row=1, column=1, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_answer = EntryFrame(self.body, 275, 50,"Cual es tu comida favorita?")
        self.security_answer.grid(row=2, column=1, pady=5, padx=15 , sticky='w')

        # Create the register button
        registrarse_button = button_frame(self.footer, 'Registrarse', None, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        registrarse_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        


#$------------------------ Main App
App=ctk.CTk()
App.title('Nibble') # Set the title of the app
App.iconbitmap('Nibble/recursos/logo/Nibble.ico') # Set the icon of the app
App.after(50, lambda: App.state('zoomed')) # Maximize the app
App.minsize(900, 700) # Set the minimum size of the app

#*------------------------ Img background from login section
img = ctk.CTkImage(Image.open('Nibble/recursos/background.jpg'), size=(1920,1080))
img_label = ctk.CTkLabel(App, image=img)
img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#*------------------------ Background frame
background = Sections(App, 720, 615, 50, '#eafbff', 'transparent', ['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'])
background.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#*------------------------ Login
Login_window = LoginLayout(background)
Login_window.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#------------------------ Run the app
App.mainloop()
