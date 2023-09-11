'''App for managing data from a School'''


import tkinter as tk # Import the tkinter module
from tkinter import messagebox # Import the messagebox module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections, EntryFrame, button_frame # Import the Sections class from modules.py
from PIL import Image # Import the Image modules from PIL

#todo - Sidebar con un .pack y cuando se pase el mouse se aumente el tamaño horizontalmente, los labels ya estaran creados
#todo - Los credenciales hay que programarlos al final con la Base de datos

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


#^------------Loginto Forgot credentials
def loginto_forgot_credentials(parent):
    '''Show a two options window and then change the layout to forgot credentials'''
    options = tk.Toplevel(parent, bg='#eeeeee')
    options.title('Olvide mis credenciales') # Set the title of the app
    options.iconbitmap('Nibble/recursos/logo/Nibble.ico') # Set the icon of the app
    options.resizable(False, False) # Disable the resize of the window

    # center the window
    window_width = int(options.winfo_screenwidth()/2 - options.winfo_reqwidth()/2)
    window_height = int(options.winfo_screenheight()/2 - options.winfo_reqheight()/2)
    options.geometry(f"400x100+{window_width}+{window_height}")

    # Create the label
    label = ctk.CTkLabel(options, text="Seleccione una opcion", font=('Arial', 20), bg_color='#eeeeee', text_color='#000000')
    label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    # create a frame for the buttons
    options_frame = Sections(options, 400, 100)
    options_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    # Create the buttons
    forgot_user = button_frame(options_frame, 'Usuario', lambda: select_option("user"), True, 'transparent', '#47959b', 28,100, font=('Arial', 15, 'bold'))
    forgot_user.grid(row=1, column=0, pady=5, padx=5 , sticky='w')

    forgot_password = button_frame(options_frame, 'Contraseña', lambda: select_option("password"), True, 'transparent', '#47959b', 28,100, font=('Arial', 15, 'bold'))
    forgot_password.grid(row=1, column=1, pady=5, padx=5 , sticky='w')

    def select_option(option):
        '''Select the option and destroy the window'''
        parent.destroy()
        ForgotCredentialsLayout(background, option).place(relx=0.5, rely=0.5, anchor=tk.CENTER)


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
        self.user = EntryFrame(self.body, 450, 50,"Usuario      ", placeholder="Usuario")
        self.user.grid(row=0, column=0, pady=0, padx=20, sticky='e')

        # Password show/hide img
        self.show = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-show.png'), size=(30,20))
        self.hide = ctk.CTkImage(Image.open('Nibble/recursos/icons/Password-hide.png'), size=(30,20))
        pass_img = { 'show': self.show, 'hide': self.hide} # Create the dictionary

        # Create the password entry frame
        self.password = EntryFrame(self.body, 450, 50,"Contraseña", True, pass_img['hide'], self.show_password, placeholder="Contraseña")
        self.password.grid(row=1, column=0, pady=0, padx=20 , sticky='e')
        self.password.entry.configure(show='*') # Hide the password

        # Create the forgot credentials button
        fg_credentials = button_frame(self.body, text='Olvide mis credenciales.', command= lambda: loginto_forgot_credentials(self) ,hover=False, txcolor='#47959b')
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
        self.user = EntryFrame(self.body, 275, 50,"Usuario      ", placeholder="Usuario")
        self.user.grid(row=0, column=0, pady=5, padx=20, sticky='e')

        # Create the email entry frame
        self.email = EntryFrame(self.body, 275, 50,"Correo electronico", placeholder="Correo electronico")
        self.email.grid(row=1, column=0, pady=5, padx=20 , sticky='e')

        # Create the password entry frame
        self.password = EntryFrame(self.body, 275, 50,"Contraseña", False, placeholder="Contraseña")
        self.password.grid(row=2, column=0, pady=5, padx=20 , sticky='e')

        # Create the confirm password entry frame
        self.confirm_password = EntryFrame(self.body, 275, 50,"Confirmar contraseña", False, placeholder="Confirmar contraseña")
        self.confirm_password.grid(row=3, column=0, pady=5, padx=20 , sticky='e')


        # Create security question entry frame
        self.security_question = EntryFrame(self.body, 275, 50,"¿Cual es tu color favorito?", placeholder="Color favorito")
        self.security_question.grid(row=0, column=1, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_answer = EntryFrame(self.body, 275, 50,"¿Cual es tu deporte favorito?", placeholder="Deporte favorito")
        self.security_answer.grid(row=1, column=1, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_answer = EntryFrame(self.body, 275, 50,"¿Cual es tu comida favorita?", placeholder="Comida favorita")
        self.security_answer.grid(row=2, column=1, pady=5, padx=15 , sticky='w')

        #*----------------------------------------- footer widgets
        # Create the register button
        registrarse_button = button_frame(self.footer, 'Registrarse', None, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        registrarse_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



#^------------forgot credentials Layout
class ForgotCredentialsLayout(ctk.CTkFrame):
    '''Forgot credentials Layout'''
    def __init__(self, parent, op):
        super().__init__(
            master = parent,
            width=720,
            height=615,
            corner_radius=50,
            fg_color='transparent',
            bg_color='transparent',
            background_corner_colors=['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'],
        )
        #*----------------------------------------- variables
        self.option = op

        #*----------------------------------------- frames
        # Create the header frame
        self.header = Sections(self, 680, 100, fcolor='transparent', bcolor='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = Sections(self, 680, 400, fcolor='transparent', bcolor='transparent',radius=25,bdcolor='#d4d4d4',border_width=2)
        self.body.place(relx=0.5, rely=0.60, anchor=tk.S)

        # Create the footer frame
        self.footer = Sections(self, 680, 80, fcolor='transparent', bcolor='transparent')
        self.footer.place(relx=0.5, rely=0.92, anchor=tk.S)


        #*----------------------------------------- header widgets
        # Create the back button
        back_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/back.png'), size=(30,30))
        back_button = button_frame(self.header,"", lambda: back_to_login(self),True,'transparent','transparent',30,30,img= back_img)
        back_button.place(relx=0.05, rely=0.5, anchor=tk.CENTER)

        # Create the Forgot credentials label
        tittle_label = ctk.CTkLabel(self.header, text="Olvide mis credenciales", font=('Arial', 30, "bold"), bg_color='transparent', text_color='#000000')
        tittle_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #*----------------------------------------- body widgets
        # Create the security question label
        security_question_label = ctk.CTkLabel(self.body, text="Preguntas de seguridad:", font=('Arial', 15, "bold"), bg_color='transparent', text_color='#000000')
        security_question_label.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Create the email entry frame
        self.email = EntryFrame(self.body, 280, 50,"Correo electronico:               ", layout=2, placeholder="Correo electronico")
        self.email.grid(row=1, column=0, pady=5, padx=20 , sticky='w')


        # Create security question entry frame
        self.security_question1 = EntryFrame(self.body, 280, 50,"¿Cual es tu color favorito?    ", layout=2, placeholder="Color favorito")
        self.security_question1.grid(row=2, column=0, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_question2 = EntryFrame(self.body, 280, 50,"¿Cual es tu deporte favorito?", layout=2, placeholder="Deporte favorito")
        self.security_question2.grid(row=3, column=0, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_question3 = EntryFrame(self.body, 280, 50,"¿Cual es tu comida favorita?", layout=2, placeholder="Comida favorita")
        self.security_question3.grid(row=4, column=0, pady=5, padx=15 , sticky='w')

        #*----------------------------------------- footer widgets
        # Create the continue button
        continue_button = button_frame(self.footer, 'Continuar', lambda: entry_add(self), True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        continue_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


                #*------------------------ Class Functions
        def entry_add(self):
            '''add to the body the entry frame (pass or user), depending on the variable'''
            self.body.place_forget()
            self.body = Sections(self, 680, 400, fcolor='transparent', bcolor='transparent',radius=25,bdcolor='#d4d4d4',border_width=2)
            self.body.place(relx=0.5, rely=0.60, anchor=tk.S)

            if self.option == 'user':
                # Create the user entry frame
                self.user = EntryFrame(self.body, 280, 50,"Usuario:               ", layout=2, placeholder="Usuario")
                self.user.grid(row=0, column=0, pady=5, padx=20, sticky='w')
                # reconfigure the button
                continue_button.configure(command=lambda: print('user'))
            elif self.option == 'password':
                # Create the password entry frame
                self.password = EntryFrame(self.body, 280, 50,"Contraseña:               ", layout=2, placeholder="Contraseña")
                self.password.grid(row=0, column=0, pady=5, padx=20 , sticky='w')
                # reconfigure the button
                continue_button.configure(command=lambda: print('password'))


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
