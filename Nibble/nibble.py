'''App for managing data from a School'''


import tkinter as tk # Import the tkinter module
from tkinter import messagebox, filedialog # Import the messagebox and filedialog modules
import datetime # Import the datetime module
import tkcalendar # Import the tkcalendar module
import customtkinter as ctk # Import the customtkinter module
from modules import EntryFrame, ButtonFrame, EventsFrame # Import the Sections class from modules.py
from PIL import Image, ImageTk # Import the Image modules from PIL

#TODO - Los credenciales hay que programarlos al final con la Base de datos
#TODO - Eliminar el modo de seleccion 

#$------------------------ Functions
#^===================================================Back to login
def back_to_login(parent):
    '''Change the layout to login'''
    parent.destroy()
    LoginLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)



#$------------------------ Classes
#^===================================================Login Layout
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
        self.header = ctk.CTkFrame(self, 680, 200, fg_color='transparent', bg_color='transparent')
        self.header.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        # Create the body frame
        self.body = ctk.CTkFrame(self, 620, 300, fg_color='transparent', bg_color='transparent')
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
        fg_credentials = ctk.CTkButton(self.body, text='Olvide mis credenciales.', command= self.loginto_forgot_credentials, hover=False, text_color='#47959b', fg_color='transparent', bg_color='transparent')
        fg_credentials.grid(row=2, column=0, pady=0, padx=20 , sticky='w')

        #*----------------------------------------- footer widgets
        # Create the register button
        registrarse_button = ctk.CTkButton(self.body, text='Registrarse', command= self.loginto_register,fg_color='#47959b', bg_color='transparent', font=('Arial', 15, 'bold'))
        registrarse_button.grid(row=3, column=0, pady=25, padx=20 , sticky='w')

        # Create the login button
        self.credentials = {"user": "admin", "password": "1234"} # Credentials dictionary
        ingresar_button = ctk.CTkButton(self.body, height=35 ,text='Ingresar', command= self.validate_entry,fg_color='#47959b', bg_color='transparent', font=('Arial', 15, 'bold'))
        ingresar_button.grid(row=3, column=0, pady=0, padx=20 , sticky='e')

        #*----------------------------------------- Events
        # When the user press enter in the password entry
        self.password.entry.bind('<Return>', lambda event: self.validate_entry())
        self.user.entry.bind('<Return>', lambda event: self.validate_entry())


    #*------------------------ Class Functions
    def show_password(self):
        '''Show the password'''
        if self.password.entry.cget('show') == '*':
            self.password.entry.configure(show='')
            self.password.button.configure(image=self.show)
        else:
            self.password.entry.configure(show='*')
            self.password.button.configure(image=self.hide)

    def validate_entry(self):
        '''Validate the entrys'''
        if self.user.entry.get() == '' or self.password.entry.get() == '':
            messagebox.showerror('Campos Vacios', 'Por favor ingrese todos los datos')
        else:
            self.loginto_app(self.credentials)

    def get_data(self):
        '''Get data from the entry frames and save it in a variable'''
        self.credentials['user'] = self.user.entry.get()
        self.credentials['password'] = self.password.entry.get()

    #*===================================================Login to app
    def loginto_app(self, credentials: dict):
        '''Check if the credentials are correct'''
        if credentials['user'] == self.user.entry.get() and credentials['password'] == self.password.entry.get():
            self.loginto_mode_selection()
        else:
            messagebox.showerror('Error', 'Usuario o contraseña incorrectos')

    #*===================================================Loginto Register
    def loginto_register(self):
        '''Change the layout to register'''
        self.destroy()
        RegisterLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #*===================================================Loginto Forgot credentials
    def loginto_forgot_credentials(self):
        '''Show a two options window and then change the layout to forgot credentials'''
        options = tk.Toplevel(self, bg='#eeeeee')
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
        options_frame = ctk.CTkFrame(options, 400, 100, fg_color='transparent', bg_color='transparent')
        options_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Create the buttons
        forgot_user = ctk.CTkButton(options_frame, 100, 28, text='Usuario', command= lambda: select_option("user"),fg_color='#47959b', bg_color='transparent', font=('Arial', 15, 'bold'))
        forgot_user.grid(row=1, column=0, pady=5, padx=5 , sticky='w')

        forgot_password = ctk.CTkButton(options_frame, 100, 28, text='Contraseña', command= lambda: select_option("password"),fg_color='#47959b', bg_color='transparent', font=('Arial', 15, 'bold'))
        forgot_password.grid(row=1, column=1, pady=5, padx=5 , sticky='w')

        def select_option(option):
            '''Select the option and destroy the window'''
            self.destroy()
            ForgotCredentialsLayout(background, option).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #*===================================================Loginto Mode Selection
    def loginto_mode_selection(self):
        '''Change the layout to mode selection'''
        self.destroy()
        ModeSelectionLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)



#^===================================================Register Layout
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
        self.header = ctk.CTkFrame(self, 680, 100, fg_color='transparent', bg_color='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = ctk.CTkFrame(self, 680, 400, fg_color='transparent', bg_color='transparent')
        self.body.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        # Create the footer frame
        self.footer = ctk.CTkFrame(self, 680, 80, fg_color='transparent', bg_color='transparent')
        self.footer.place(relx=0.5, rely=0.92, anchor=tk.S)


        #*----------------------------------------- header widgets
        # Create the back button
        back_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/back.png'), size=(30,30))
        back_button = ctk.CTkButton(self.header, 30, 30, text='', command= lambda: back_to_login(self),fg_color='transparent', bg_color='transparent', image=back_img)
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
        self.security_answer1 = EntryFrame(self.body, 275, 50,"¿Cual es tu color favorito?", placeholder="Color favorito")
        self.security_answer1.grid(row=0, column=1, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_answer2 = EntryFrame(self.body, 275, 50,"¿Cual es tu deporte favorito?", placeholder="Deporte favorito")
        self.security_answer2.grid(row=1, column=1, pady=5, padx=15 , sticky='w')

        # Create security answer entry frame
        self.security_answer3 = EntryFrame(self.body, 275, 50,"¿Cual es tu comida favorita?", placeholder="Comida favorita")
        self.security_answer3.grid(row=2, column=1, pady=5, padx=15 , sticky='w')

        #*----------------------------------------- footer widgets
        # Create the register button
        registrarse_button = ctk.CTkButton(self.footer, height=35, text='Registrarse', command= self.validate_entry,fg_color='#47959b', bg_color='transparent', font=('Arial', 15, 'bold'))
        registrarse_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    #*------------------------ Class Functions
    def validate_entry(self):
        '''Validate the entrys'''
        if self.user.entry.get() == '' or self.email.entry.get() == '' or self.password.entry.get() == '' or self.confirm_password.entry.get() == '' or self.security_answer1.entry.get() == '' or self.security_answer2.entry.get() == '' or self.security_answer3.entry.get() == '':
            messagebox.showerror('Campos Vacios', 'Por favor ingrese todos los datos')
        elif self.password.entry.get() != self.confirm_password.entry.get():
            messagebox.showerror('Contraseñas no coinciden', 'Las contraseñas no coinciden')
        else:
            # TODO - Save the register data in the database
            back_to_login(self)




#^===================================================forgot credentials Layout
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
        self.header = ctk.CTkFrame(self, 680, 100, fg_color='transparent', bg_color='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = ctk.CTkFrame(self, 680, 400, fg_color='transparent', bg_color='transparent', corner_radius=25, border_color='#d4d4d4', border_width=2)
        self.body.place(relx=0.5, rely=0.60, anchor=tk.S)

        # Create the footer frame
        self.footer = ctk.CTkFrame(self, 680, 80, fg_color='transparent', bg_color='transparent')
        self.footer.place(relx=0.5, rely=0.92, anchor=tk.S)


        #*----------------------------------------- header widgets
        # Create the back button
        back_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/back.png'), size=(30,30))
        back_button = ctk.CTkButton(self.header, 30, 30, text='', command= lambda: back_to_login(self),fg_color='transparent', bg_color='transparent', image=back_img)
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
        self.continue_button = ctk.CTkButton(self.footer, height=35, text='Continuar', command= self.validate_entry,fg_color='#47959b', bg_color='transparent', font=('Arial', 15, 'bold'))
        self.continue_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


            #*------------------------ Class Functions
    def entry_add(self):
        '''add to the body the entry frame (pass or user), depending on the variable'''
        if self.option == 'user':
            # Create the user label
            user_credentials = ctk.CTkLabel(self.footer, text="Usuario: " + "admin", font=('Arial', 15), bg_color='transparent', text_color='#000000')
            user_credentials.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
            # reconfigure the button
            self.continue_button.configure(text='Volver al login', command=lambda: back_to_login(self))
        elif self.option == 'password':
            self.body.place_forget()
            self.body = ctk.CTkFrame(self, 680, 400, fg_color='transparent', bg_color='transparent', corner_radius=25, border_color='#d4d4d4', border_width=2)
            self.body.place(relx=0.5, rely=0.60, anchor=tk.S)
            # Create the password entry frame
            self.password_credentials = EntryFrame(self.body, 280, 50,"Contraseña:               ", layout=2, placeholder="Contraseña")
            self.password_credentials.grid(row=0, column=0, pady=5, padx=20 , sticky='w')
            # reconfigure the button
            self.continue_button.configure(text='Volver al login', command=self.validate_pass)

    def validate_entry(self):
        '''Validate the entrys'''
        if self.email.entry.get() == '' or self.security_question1.entry.get() == '' or self.security_question2.entry.get() == '' or self.security_question3.entry.get() == '':
            messagebox.showerror('Campos Vacios', 'Por favor ingrese todos los datos')
        else:
            self.entry_add()

    def validate_pass(self):
        '''Validate the entrys'''
        if self.password_credentials.entry.get() == '':
            messagebox.showerror('Campos Vacios', 'Por favor ingrese todos los datos')
        else:
            # TODO - Change the password
            back_to_login(self)




#^===================================================Mode Selection Layout
class ModeSelectionLayout(ctk.CTkFrame):
    '''Mode Selection Layout'''
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
        self.header = ctk.CTkFrame(self, 680, 100, fg_color='transparent', bg_color='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = ctk.CTkFrame(self, 680, 400, fg_color='transparent', bg_color='transparent')
        self.body.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        #*----------------------------------------- header widgets
        # Create the back button
        back_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/back.png'), size=(30,30))
        back_button = ctk.CTkButton(self.header, 30, 30, text='', command= lambda: back_to_login(self),fg_color='transparent', bg_color='transparent', image=back_img)
        back_button.place(relx=0.05, rely=0.5, anchor=tk.CENTER)

        # Create the Hello Label
        # TODO - Put the name of the user (Buenos Dias, User)
        # If is morning (6:00 - 12:00) say good morning
        if datetime.datetime.now().hour >= 6 and datetime.datetime.now().hour < 12:
            hello_label = ctk.CTkLabel(self.header, text="Buenos dias", font=('Arial', 45, "bold"), bg_color='transparent', text_color='#243233')
        # If is afternoon (12:00 - 18:00) say good afternoon
        elif datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 18:
            hello_label = ctk.CTkLabel(self.header, text="Buenas tardes", font=('Arial', 45, "bold"), bg_color='transparent', text_color='#243233')
        # If is night (18:00 - 6:00) say good night
        else:
            hello_label = ctk.CTkLabel(self.header, text="Buenas noches", font=('Arial', 45, "bold"), bg_color='transparent', text_color='#243233')
        hello_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #*----------------------------------------- body widgets
        # Create the label for the mode selection
        mode_label = ctk.CTkLabel(self.body, text="Seleccion de modo:", font=('Arial', 25, "bold"), bg_color='transparent', text_color='#000000')
        mode_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        # Create the frame for the buttons
        buttons_frame = ctk.CTkFrame(self.body, 680, 300, fg_color='transparent', bg_color='transparent')
        buttons_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Create the button Liceo
        liceo_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/highschool2.png'), size=(200,200))
        liceo_button = ctk.CTkButton(buttons_frame, 150, 150, text='', command= self.loginto_highschool_mode,fg_color='transparent', bg_color='transparent', image=liceo_img)
        liceo_button.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Create the button Colegio
        colegio_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/school2.png'), size=(200,200))
        colegio_button = ctk.CTkButton(buttons_frame, 150, 150, text='', command= self.loginto_school_mode,fg_color='transparent', bg_color='transparent', image=colegio_img)
        colegio_button.grid(row=0, column=1, pady=5, padx=20, sticky='w')

            #*------------------------ Class Functions

    #*===================================================Loginto school mode
    def loginto_school_mode(self):
        '''Change the layout to mode selection'''
        img_label.destroy()
        background.destroy()
        self.destroy()
        new_background = ctk.CTkFrame(App, corner_radius=0, fg_color='#eafbff', bg_color='transparent')
        new_background.place(relx=0, rely=0, relwidth=1, relheight=1)
        school = AppLayout(new_background)
        school.place(relx=0, rely=0, relwidth=1, relheight=1)

    #*===================================================Loginto highschool mode
    def loginto_highschool_mode(self):
        '''Change the layout to mode selection'''
        img_label.destroy()
        background.destroy()
        self.destroy()
        new_background = ctk.CTkFrame(App, corner_radius=0, fg_color='#eafbff', bg_color='transparent')
        new_background.place(relx=0, rely=0, relwidth=1, relheight=1)




#^===================================================App Layout
class AppLayout(ctk.CTkFrame):
    '''Layout of the app'''
    def __init__(self, master):
        super().__init__(
            master = master,
            bg_color='#f5fdff',
            fg_color='transparent',
            )

        #* ------------------------ Frames
        # Create the header frame
        self.header = ctk.CTkFrame(self, fg_color='#f5fdff', bg_color='#f5fdff')
        self.header.place(relx=0.13, rely=0, relwidth=0.87, relheight=0.1)

        # Create the sidebar frame
        self.sidebar = ctk.CTkFrame(self, fg_color='#f5fdff', bg_color='#f5fdff')
        self.sidebar.place(relx=0, rely=0, relwidth=0.13, relheight=1)

        # Create the body frame
        self.body = ctk.CTkFrame(self, fg_color='#f5f5f5', bg_color='#f5fdff', border_color='#c2c9db', border_width=1.3)
        self.body.place(relx=0.13, rely=0.1, relwidth=0.87, relheight=0.9)

        #* ------------------------ Header
        # Header title
        self.title = ctk.CTkLabel(
            master = self.header,
            text = 'Unidad Educativa Salvador Garmendia Grateron',
            font = ('Arial', 40, 'bold'),
            text_color='#243233',
            )
        self.title.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        #* ------------------------ Sidebar
        # --------------- Sidebar NIBBLE ICON
        # Create the logo image and label
        self.logo_img = ctk.CTkImage(Image.open('Nibble/recursos/logo/Nibble-Logo-2.png'), size=(130,40))
        self.logo_img2 = ctk.CTkImage(Image.open('Nibble/recursos/logo/Nibble-Logo-1.png'), size=(40,40))
        self.logo_label = ctk.CTkLabel(self.sidebar, image=self.logo_img, corner_radius=50, text="", fg_color='#f5fdff', bg_color='#f5fdff')
        self.logo_label.pack(pady=15, padx=10, side=tk.TOP, anchor=tk.W)

        # --------------- Sidebar buttons
        # Home button
        home_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/home.png'), size=(40,40))
        self.home_button = ButtonFrame(self.sidebar,"Inicio                 ",'transparent','#cdd8f5', lambda: self.change_layout(0),30,30,True,font=('Arial', 14), txcolor='#32464b',img= home_img, hover_color='#cdd8f5', layout=2)
        self.home_button.pack(fill = tk.X, pady=5, padx=10, side=tk.TOP)

        # Teachers button
        teachers_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/teachers.png'), size=(40,40))
        self.teachers_button = ButtonFrame(self.sidebar,"Profesores         ",command=lambda: self.change_layout(1),size_x=30,size_y=30,font=('Arial', 14), txcolor='#32464b',img= teachers_img, hover_color='#cdd8f5', layout=2)
        self.teachers_button.pack(fill = tk.X, pady=5, padx=10, side=tk.TOP)

        # Students button
        students_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/student.png'), size=(40,40))
        self.students_button = ButtonFrame(self.sidebar,"Estudiantes        ",command= lambda: self.change_layout(2),size_x=30,size_y=30,font=('Arial', 14), txcolor='#32464b',img= students_img, hover_color='#cdd8f5', layout=2)
        self.students_button.pack(fill = tk.X, pady=5, padx=10, side=tk.TOP)

        # Grades button
        grades_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/grades.png'), size=(40,40))
        self.grades_button = ButtonFrame(self.sidebar,"Notas                 ",command=lambda: self.change_layout(3),size_x=30,size_y=30,font=('Arial', 14), txcolor='#32464b',img= grades_img, hover_color='#cdd8f5', layout=2)
        self.grades_button.pack(fill = tk.X, pady=5, padx=10, side=tk.TOP)

        # Schedule button
        schedule_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/schedule.png'), size=(40,40))
        self.schedule_button = ButtonFrame(self.sidebar,"Horario               ",command=lambda: self.change_layout(4),size_x=30,size_y=30,font=('Arial', 14), txcolor='#32464b',img= schedule_img, hover_color='#cdd8f5', layout=2)
        self.schedule_button.pack(fill = tk.X, pady=5, padx=10, side=tk.TOP)

        # Change Mode button
        change_mode_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/change_mode_dark.png'), size=(40,40))
        self.change_mode_button = ButtonFrame(self.sidebar,"Cambiar modo   ",command=lambda: print('Change Mode'),size_x=30,size_y=30,font=('Arial', 14), txcolor='#32464b',img= change_mode_img, hover_color='#cdd8f5', layout=3)
        self.change_mode_button.pack(fill = tk.X, pady=5, padx=10, side=tk.BOTTOM)


        #* ------------------------ Body
        HomeLayout(self.body).place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.95, relheight=0.95)

        self.responsive = True

        #! ------------------------ MAYBE WE DONT NEED THIS
        #*------------------------ Events
        # Responsive design
        # self.bind('<Configure>', lambda event: self.responsive_design())

    #*---------------------------------------------- Functions
    def change_layout(self, layout):
        '''Change the layout of the body'''
        # Destroy the body
        self.body.place_forget()
        self.body.place(relx=0.13, rely=0.1, relwidth=0.87, relheight=0.9)

        case = {
            0: HomeLayout(self.body),
            1: TeachersLayout(self.body),
            2: StudentsLayout(self.body),
            3: GradesLayout(self.body),
            4: ScheduleLayout(self.body),
        }

        case[layout].place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.95, relheight=0.95)

        buttons = (self.home_button, self.teachers_button, self.students_button, self.grades_button, self.schedule_button)

        for button in buttons:
            if buttons.index(button) == layout:
                button.button.configure(fg_color='#cdd8f5')
            else:
                button.button.configure(fg_color='transparent')


    #! ------------------------ MAYBE WE DONT NEED THIS
    # def responsive_design(self):
    #     "Eliminate the button's text when the app size is below 1520x850"
    #     if self.responsive:
    #         if App.state() == 'normal':
    #             self.home_button.button.configure(text='')
    #             self.teachers_button.button.configure(text='')
    #             self.students_button.button.configure(text='')
    #             self.grades_button.button.configure(text='')
    #             self.schedule_button.button.configure(text='')
    #             self.change_mode_button.button.configure(text='')
    #             self.logo_label.configure(image=self.logo_img2)
    #             self.responsive = False
    #     else:
    #         if App.state() == 'zoomed':
    #             self.home_button.button.configure(text="Inicio                 ")
    #             self.teachers_button.button.configure(text="Profesores         ")
    #             self.students_button.button.configure(text="Estudiantes        ")
    #             self.grades_button.button.configure(text="Notas                 ")
    #             self.schedule_button.button.configure(text="Horario               ")
    #             self.change_mode_button.button.configure(text="Cambiar modo   ")
    #             self.logo_label.configure(image=self.logo_img)
    #             self.responsive = True





#^===================================================Home Layout
class HomeLayout(ctk.CTkFrame):
    '''Home Layout (Calendar, identifier label)'''
    def __init__(self, master):
        super().__init__(
            master = master,
            bg_color='#f5f5f5',
            fg_color='transparent',
        )

        #* ------------------------ Frames
        # Create the body frame
        self.body = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent')
        self.body.place(relx=0.5, rely=0.4,anchor = tk.CENTER,relwidth=0.7, relheight=0.7)

        # Create the footer frame
        self.footer = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent')
        self.footer.place(relx=0.5, rely=0.85,anchor = tk.CENTER, relwidth=0.7, relheight=0.2)

        #* ------------------------ Body
        # Create The Calendar
        self.calendar = tkcalendar.Calendar(
            self.body,
            font=('Arial', 15),
            selectmode='day',
            locale='es_ES',
            date_pattern='dd/mm/yyyy',
            showweeknumbers=False,
            background='#0d1321',
            foreground='#ffffff',
            headersbackground='#748cab',
            normalbackground='#f8f9fa',
            normalforeground='#000000',
            weekendbackground='#adb5bd',
            weekendforeground='#000000',
            othermonthbackground='#ced4da',
            othermonthforeground='#000000',
            othermonthwebackground='#ced4da',
            othermonthweforeground='#000000',
            bordercolor='#ced4da',
            borderwidth=1,
            )
        self.calendar.place(relx=0.5, rely=0, anchor=tk.N, relwidth=1, relheight=1)

        # Button to show the events
        self.event_button = ctk.CTkButton(self.body, height=35, text='Eventos', command=self.event, fg_color='#47959b', bg_color='#0d1321', font=('Arial', 15, 'bold'))
        self.event_button.place(relx=0.5, rely=0.029, anchor=tk.CENTER, relwidth=0.25, relheight=0.05)

        # Label to show the event
        self.event_label = ctk.CTkLabel(self.footer, text="", font=('Arial', 15, "bold"), bg_color='transparent', text_color='#000000')
        self.event_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Bind the calendar to the label
        self.calendar.bind('<<CalendarSelected>>', self.change_label)

    def change_label(self, event):
        '''Change the label text'''
        # Get date
        date = self.calendar.selection_get()
        # Get the events
        event_clicked = self.calendar.get_calevents(date)

        if len(event_clicked) > 1:
            # Get the text of the events
            text = ""
            # For each event to 3
            for events in range(3):
                # Add the text to the label
                text += str(events+1) + ". " + self.calendar.calevent_cget(event_clicked[events], 'text') + '\n'
            # Change the text of the label
            self.event_label.configure(text=text)
        elif len(event_clicked) == 1:
            # Get the text of the event
            text = self.calendar.calevent_cget(event_clicked[0], 'text')
            # Change the text of the label
            self.event_label.configure(text=text)
        else:
            # Change the text of the label
            self.event_label.configure(text="")


    def event (self):
        '''Events manager Layout'''
        # Get date
        date = self.calendar.selection_get()

        # disable the button
        self.event_button.configure(state=tk.DISABLED)

        # Create the window
        window = tk.Toplevel(
                        master=self,
                        bg='#f5f5f5',
                        width=1000,
                        height=800,
                        )
        window.title('Eventos') # Set the title of the app
        window.iconbitmap('Nibble/recursos/logo/Nibble.ico')
        window.resizable(False, False)
        window.propagate(False)

        # Center the window
        x = (window.winfo_screenwidth() / 2) - (1000 / 2)
        y = (window.winfo_screenheight() / 2) - (800 / 2)
        window.geometry(f'{1000}x{800}+{int(x)}+{int(y)}')

        # on close window activate the button
        window.bind('<Destroy>', lambda event: self.event_button.configure(state=tk.NORMAL))

        #* ------------------------ Frames
        # Create the Form frame
        form_frame = ctk.CTkFrame(window,bg_color='transparent', fg_color='transparent')
        form_frame.place(relx=0, rely=0, relwidth=1, relheight=0.4)

        # Create the Search frame
        search_frame = ctk.CTkFrame(window,height=50,bg_color='transparent', fg_color='transparent')
        search_frame.place(relx=0, rely=0.4, relwidth=1, relheight=0.1)

        # Create the Scroll_events frame ------------------------ Scrollable frame
        scroll_frame = ctk.CTkFrame(window,bg_color='transparent', fg_color='transparent')
        scroll_frame.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.48)

        # Create the Scrollbar
        scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the Canvas
        canvas = tk.Canvas(scroll_frame, bg=None, bd=0, highlightthickness=0, yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Configure the scrollbar
        scrollbar.config(command=canvas.yview)

        # Create the Scrollable frame
        events_frame = ctk.CTkFrame(canvas, bg_color='transparent', fg_color='transparent')
        events_frame.pack(fill=tk.BOTH, expand=True)

        # Configure the canvas
        canvas.create_window((0,0), window=events_frame, anchor=tk.NW)

        # Bind the scrollbar to the canvas
        events_frame.bind('<Configure>', lambda event: canvas.configure(scrollregion=canvas.bbox('all')))


        #* ------------------------ Form - widgets
        # Label
        tittle_label = ctk.CTkLabel(form_frame, text="Crear un evento", font=('Arial', 30, "bold"), bg_color='transparent', fg_color=None,text_color='#000000')
        tittle_label.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Tittle entry
        window.event_name = EntryFrame(form_frame, 500, 50,"Nombre del evento", placeholder="Nombre del evento")
        window.event_name.grid(row=1, column=0, pady=5, padx=20, sticky='w')

        # Description entry
        window.description = EntryFrame(form_frame, 500, 50,"Descripcion", placeholder="Descripcion")
        window.description.grid(row=2, column=0, pady=5, padx=20, sticky='w')

        # Date entry
        window.date_entry = EntryFrame(form_frame, 200, 50,"Fecha", placeholder="Fecha", another=True, command=lambda: self.datepicker(window))
        window.date_entry.grid(row=1, column=1, pady=5, padx=20, sticky='e')
        window.date_entry.entry.insert(0, date.strftime('%d / %m / %Y'))
        window.date_entry.entry.configure(state='readonly')

        # Separator line
        separator_line = ctk.CTkLabel(form_frame, text="",bg_color='#000000')
        separator_line.place(relx=0.5, rely=1, anchor=tk.CENTER, relwidth=0.95, relheight=0.01)

        #* ------------------------ def Functions

        def validate_entries():
            '''Validate the entries'''
            if window.event_name.entry.get() == '' or window.description.entry.get() == '':
                messagebox.showerror('Campos Vacios', 'Por favor ingrese todos los datos', parent=window)
            else:
                # TODO - Save the event data in the database
                create_event(window.event_name.entry.get(), window.description.entry.get())

        def create_event(name, description):
            '''Create the event'''
            # get the date
            date = window.date_entry.entry.get()
            # turn the date into a datetime object without the time
            date = datetime.datetime.strptime(date, '%d / %m / %Y').date()

            # Create the event
            window.event_button.configure(text = 'Crear', command=validate_entries)
            self.calendar.calevent_create(date, name, description)
            EventsFrame(events_frame, name, description, date, self.calendar, window, create_event).pack(fill=tk.X, pady=5, padx=0, side=tk.TOP)
            # Clear the entries
            window.event_name.entry.delete(0, tk.END)
            window.description.entry.delete(0, tk.END)
            window.date_entry.entry.delete(0, tk.END)


        # EVent button
        window.event_button = ctk.CTkButton(form_frame,width=100, height=34 ,text='Crear', command= validate_entries,font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        window.event_button.grid(row=2, column=1, pady=5, padx=20, sticky='se')

        #* ------------------------ Search - widgets
        # Search entry
        search_entry = EntryFrame(search_frame, 600, 50,"Buscar", placeholder="Fecha o nombre del evento", layout=2, another=True)
        search_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #* ------------------------ Scroll_events - widgets

        # frame tittles
        tittle_frame = ctk.CTkFrame(scroll_frame, bg_color='transparent', fg_color='#dce0e4', border_color='#c2c9db', border_width=1.3)
        tittle_frame.place(relx=0, rely=0, relwidth=0.98, relheight=0.1)

        # Create the tittle label
        tittle_label = ctk.CTkLabel(tittle_frame, text="Titulo", font=('Arial', 20, "bold"), bg_color='#dce0e4', fg_color=None,text_color='#243233')
        tittle_label.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

        # Create the description label
        description_label = ctk.CTkLabel(tittle_frame, text="Descripcion", font=('Arial', 20, "bold"), bg_color='#dce0e4', fg_color=None,text_color='#243233')
        description_label.place(relx=0.4, rely=0.5, anchor=tk.CENTER)

        # Create the date label
        date_label = ctk.CTkLabel(tittle_frame, text="Fecha", font=('Arial', 20, "bold"), bg_color='#dce0e4', fg_color=None,text_color='#243233')
        date_label.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

        # Create the button label
        button_label = ctk.CTkLabel(tittle_frame, text="Acciones", font=('Arial', 20, "bold"), bg_color='#dce0e4', fg_color=None,text_color='#243233')
        button_label.place(relx=0.9, rely=0.5, anchor=tk.CENTER)



        # Create a space between the tittle and the events
        ctk.CTkLabel(events_frame, text="",bg_color='transparent').pack(fill=tk.X, pady=5, padx=20, side=tk.TOP)

        def show_events():
            '''Show the events'''
            cant = len(self.calendar.calevents)
            if cant > 0:
                for event in self.calendar.calevents:
                    # Get the text, date and tag of the events
                    text = self.calendar.calevent_cget(event, 'text')
                    date = self.calendar.calevent_cget(event, 'date')
                    description = self.calendar.calevent_cget(event, 'tags')
                    # Create the event frame
                    EventsFrame(events_frame, text, description, date, self.calendar, window,create_event).pack(fill=tk.X, pady=5, padx=0, side=tk.TOP)

        show_events()

    def datepicker(self, parent):
        '''Create the datepicker'''
        # Create the window
        window = tk.Toplevel(
                        master=parent,
                        bg='#f5f5f5',
                        width=400,
                        height=300,
                        )
        window.title('Calendario') # Set the title of the app
        window.iconbitmap('Nibble/recursos/logo/Nibble.ico')
        window.resizable(False, False)
        parent.date_entry.button.configure(state='disabled')

        # Create the calendar
        calendar = tkcalendar.Calendar(
            window,
            font=('Arial', 15),
            selectmode='day',
            locale='es_ES',
            date_pattern='dd/mm/yyyy',
            showweeknumbers=False,
            )
        calendar.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=1, relheight=1)

        def update_date():
            parent.date_entry.entry.configure(state='normal')
            parent.date_entry.entry.delete(0, tk.END)
            parent.date_entry.entry.insert(0, calendar.selection_get().strftime('%d / %m / %Y'))
            parent.date_entry.entry.configure(state='readonly')
            parent.date_entry.button.configure(state='normal')
            window.destroy()

        # Bind the calendar to the entry
        calendar.bind('<<CalendarSelected>>', lambda event: update_date())







#^===================================================Teachers Layout
class TeachersLayout(ctk.CTkFrame):
    '''Teachers Layout'''
    def __init__(self, master):
        super().__init__(
            master = master,
            bg_color='#f5f5f5',
            fg_color='transparent',
        )

        #* ------------------------ Frames
        # Create the body frame left
        self.body_left = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent', border_color='#a1a1a1', border_width=1.3)
        self.body_left.place(relx=0, rely=0,relwidth=0.45, relheight=0.9)

        # Create the body frame middle
        self.body_middle = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent',  border_color='#a1a1a1', border_width=1.3)
        self.body_middle.place(relx=0.4525, rely=0,relwidth=0.245, relheight=0.9)

        # Create the body frame right
        self.body_right = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent',  border_color='#a1a1a1', border_width=1.3)
        self.body_right.place(relx=0.7, rely=0,relwidth=0.3, relheight=0.9)

        # Create the Footer frame
        self.footer = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent')
        self.footer.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)


        #* ------------------------ Body Left
        # Create the entry frame Nombre Profesor
        self.name_teacher = EntryFrame(self.body_left, 300, 50,"Nombre del Profesor", placeholder="Nombre", layout=2)
        self.name_teacher.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Apellido Profesor
        self.lname_teacher = EntryFrame(self.body_left, 300, 50,"Apellido del Profesor", placeholder="Apellido", layout=2)
        self.lname_teacher.grid(row=1, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Cedula Profesor
        self.id_teacher = EntryFrame(self.body_left, 300, 50,"Cedula del Profesor ", placeholder="Cedula", layout=2)
        self.id_teacher.grid(row=2, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Fecha de Nacimiento Profesor
        self.date_entry = EntryFrame(self.body_left, 280, 50,"Fecha de Nacimiento", placeholder="Fecha de Nacimiento", layout=2, another=True, command=lambda: HomeLayout.datepicker(self, self))
        self.date_entry.grid(row=3, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Telefono Profesor
        self.phone_teacher = EntryFrame(self.body_left, 260, 50,"Telefono del Profesor", placeholder="Telefono", layout=3)
        self.phone_teacher.grid(row=4, column=0, pady=5, padx=20, sticky='w')


        # Create the entry frame Correo Profesor
        self.email_teacher = EntryFrame(self.body_left, 510, 50,"Correo del Profesor", placeholder="Correo")
        self.email_teacher.grid(row=5, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Direccion Profesor
        self.address_teacher = EntryFrame(self.body_left, 510, 50,"Direccion del Profesor", placeholder="Direccion")
        self.address_teacher.grid(row=6, column=0, pady=5, padx=20, sticky='w')


        #* ------------------------ Body Middle
        # Create the label for the tittle
        self.tittle_label_img = ctk.CTkLabel(self.body_middle, text="Copia Del Titulo", font=('Arial', 20, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.tittle_label_img.grid(row=0, column=0, pady=5, padx=20, sticky='n')

        # add padding to the tittle
        self.body_middle.grid_rowconfigure(0, pad=20)

        # Create the button to add the college_degree
        self.college_degree_button = ctk.CTkButton(self.body_middle, width=100, height=34, text='Agregar', command= self.add_college_degree, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.college_degree_button.grid(row=1, column=0, pady=5, padx=20, sticky='n')

        # Create the button to view the college_degree
        self.view_college_degree_button = ctk.CTkButton(self.body_middle, width=100, height=34, text='Ver', command= self.view_college_degree, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.view_college_degree_button.grid(row=2, column=0, pady=5, padx=20, sticky='n')

        # Create the button to delete the college_degree
        self.delete_college_degree_button = ctk.CTkButton(self.body_middle, width=100, height=34, text='Eliminar', command= self.delete_college_degree, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.delete_college_degree_button.grid(row=3, column=0, pady=5, padx=20, sticky='n')

        # add padding to the buttons
        self.body_middle.grid_rowconfigure(3, pad=50)

        # Create the preview tittle
        self.label_preview = ctk.CTkLabel(self.body_middle, text="Vista Previa", font=('Arial', 20, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.label_preview.grid(row=4, column=0, pady=5, padx=20, sticky='n')

        # Create the preview label
        self.previmg = ctk.CTkImage(Image.open('Nibble/recursos/icons/preview.png'), size=(150,150))
        self.preview = ctk.CTkLabel(self.body_middle, text="", bg_color='transparent', image=self.previmg, fg_color='transparent', font=('Arial', 1))
        self.preview.grid(row=5, column=0, pady=5, padx=20, sticky='n')

        # center the body_middle
        self.body_middle.grid_columnconfigure(0, weight=1)


        #* ------------------------ Body Right
        # Create the label for the tittle
        self.tittle_label = ctk.CTkLabel(self.body_right, text="Asignar Materia", font=('Arial', 20, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.tittle_label.grid(row=0, column=0, pady=5, padx=20, sticky='n')

        # Create the entry frame Cedula
        self.ci_teacher = EntryFrame(self.body_right, 300, 50,"Cedula del Profesor", placeholder="Cedula")
        self.ci_teacher.grid(row=1, column=0, pady=5, padx=20, sticky='w')

        #TODO - Cambiar el textbox por un combobox
        # Create the entry frame Materia
        self.subject_teacher = EntryFrame(self.body_right, 300, 50,"Materia", placeholder="Materia")
        self.subject_teacher.grid(row=2, column=0, pady=5, padx=20, sticky='w')

        # Create the button to asign the subject
        self.asign_button = ctk.CTkButton(self.body_right, width=100, height=34, text='Asignar', command=self.asign_subject, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.asign_button.grid(row=3, column=0, pady=5, padx=20, sticky='n')


        #* ------------------------ Footer
        # Create the Search bar
        self.search_bar = EntryFrame(self.footer, 500, 50,"Buscar", placeholder="Cedula Profesor", layout=2, another=True)
        self.search_bar.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Create the button to add the teacher
        self.add_button = ctk.CTkButton(self.footer, width=100, height=34, text='Agregar', command=self.add_teacher, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.add_button.grid(row=0, column=3, pady=5, padx=20, sticky='s')

        # Create the button to save the teacher
        self.save_button = ctk.CTkButton(self.footer, width=100, height=34, text='Guardar', command=self.save_teacher, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.save_button.grid(row=0, column=2, pady=5, padx=20, sticky='s')

        # Create the button to delete the teacher
        self.delete_button = ctk.CTkButton(self.footer, width=100, height=34, text='Eliminar', command=self.delete_teacher, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.delete_button.grid(row=0, column=1, pady=5, padx=20, sticky='s')

        self.footer.grid_columnconfigure(0, weight=1)





        #* ------------------------ Functions
    def add_college_degree(self):
        '''Add the college degree img to the button'''
        img_dir = filedialog.askopenfilename(initialdir='/', title='Select a file', filetypes=(('png files', '*.png'), ('jpg files', '*.jpg'), ('jpeg files', '*.jpeg')))
        if img_dir != '':
            img_degree = ctk.CTkImage(Image.open(img_dir), size=(200,250))
            self.preview.configure(image=img_degree, text=img_dir) #TODO - delete the text

    def view_college_degree(self):
        '''Show the college degree img'''
        if self.preview.cget('image') != self.previmg:
            window = tk.Toplevel(
                            master=self,
                            bg='#2c313c',
                            )
            window.title('Preview') # Set the title of the app
            window.iconbitmap('Nibble/recursos/logo/Nibble.ico')
            window.resizable(False, False)
            window.state('zoomed')

            # Create the image
            img_show = self.preview.cget('text') #TODO - Get the image from the database
            img_show = ctk.CTkImage(Image.open(img_show), size=(900, window.winfo_screenheight() - 50))




            # Create the label
            label = ctk.CTkLabel(window, image=img_show, bg_color='transparent', fg_color='transparent', text='')
            label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        else:
            messagebox.showerror('Error', 'No hay ninguna imagen', parent=self)

    def delete_college_degree(self):
        self.preview.configure(image=self.previmg, text='')
        #TODO - Delete the college degree from the database


    def asign_subject(self):
        pass

    def add_teacher(self):
        pass

    def save_teacher(self):
        pass

    def delete_teacher(self):
        pass


#^===================================================Students Layout
class StudentsLayout(ctk.CTkFrame):
    '''Students Layout'''
    def __init__(self, master):
        super().__init__(
            master = master,
            bg_color='#f5f5f5',
            fg_color='transparent',
        )
        #* ------------------------ Frames
        # Create the body frame left
        self.body_left = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent', border_color='#a1a1a1', border_width=1.3)
        self.body_left.place(relx=0, rely=0,relwidth=0.49, relheight=0.9)

        # Create the body frame right
        self.body_right = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent', border_color='#a1a1a1', border_width=1.3)
        self.body_right.place(relx=0.5, rely=0,relwidth=0.5, relheight=0.9)

        # Create the buttons frame for body right
        self.buttons_frame = ctk.CTkFrame(self.body_right, fg_color='transparent', bg_color='transparent')
        self.buttons_frame.place(relx=0.05, rely=0.4,relwidth=0.9, relheight=0.1)

        # Create the Footer frame
        self.footer = ctk.CTkFrame(self, fg_color='transparent', bg_color='transparent')
        self.footer.place(relx=0, rely=0.9, relwidth=1, relheight=0.1)

        #* ------------------------ Body Left
        # Create the label for the tittle
        self.tittle_label_student = ctk.CTkLabel(self.body_left, text="Registrar Estudiante", font=('Arial', 20, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.tittle_label_student.grid(row=0, column=0, pady=5, padx=20, sticky='n')

        # Create the entry frame Nombre Estudiante
        self.name_student = EntryFrame(self.body_left, 350, 50,"Nombre del Estudiante", placeholder="Nombre", layout=2)
        self.name_student.grid(row=1, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Apellido Estudiante
        self.lname_student = EntryFrame(self.body_left, 350, 50,"Apellido del Estudiante", placeholder="Apellido", layout=2)
        self.lname_student.grid(row=2, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Cedula Estudiante
        self.id_student = EntryFrame(self.body_left, 350, 50,"Cedula del Estudiante ", placeholder="Cedula", layout=2)
        self.id_student.grid(row=3, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Fecha de Nacimiento Estudiante 
        self.date_entry = EntryFrame(self.body_left, 330, 50,"Fecha de Nacimiento", placeholder="Fecha de Nacimiento", layout=2, another=True, command=lambda: HomeLayout.datepicker(self, self))
        self.date_entry.grid(row=4, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Telefono Estudiante
        self.phone_student = EntryFrame(self.body_left, 280, 50,"Contactos", placeholder="Telefono", layout=3)
        self.phone_student.grid(row=5, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame address Estudiante
        self.address_student = EntryFrame(self.body_left, 580, 50,"Direccion del Estudiante", placeholder="Direccion")
        self.address_student.grid(row=6, column=0, pady=5, padx=20, sticky='w')
        
        # Create the entry frame date of admission
        self.date_admission = EntryFrame(self.body_left, 300, 50,"Fecha de Ingreso", placeholder="Fecha de Ingreso", layout=2, another=True, command=lambda: HomeLayout.datepicker(self, self))
        self.date_admission.grid(row=7, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame grade
        self.grade = EntryFrame(self.body_left, 300, 50,"Etapa (Año/Grado)", placeholder="Año/Grado", layout=2)
        self.grade.grid(row=8, column=0, pady=5, padx=20, sticky='w')

        # Create the button to change the grade
        self.change_grade_button = ctk.CTkButton(self.body_left, width=100, height=34, text='Cambiar Etapa', command=self.change_grade, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.change_grade_button.grid(row=9, column=0, pady=5, padx=20, sticky='w')

        #* ------------------------ Body Right

        # Create the label for the tittle
        self.tittle_label_Parent = ctk.CTkLabel(self.body_right, text="Registrar Representante", font=('Arial', 20, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.tittle_label_Parent.grid(row=0, column=0, pady=5, padx=20, sticky='n')

        # Create the entry frame Nombre Representante
        self.name_parent = EntryFrame(self.body_right, 450, 50,"Nombre", placeholder="Nombre Representante", layout=2)
        self.name_parent.grid(row=1, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Apellido Representante
        self.lname_parent = EntryFrame(self.body_right, 450, 50,"Apellido", placeholder="Apellido Representante", layout=2)
        self.lname_parent.grid(row=2, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Cedula Representante
        self.id_parent = EntryFrame(self.body_right, 450, 50,"Cedula  ", placeholder="Cedula Representante", layout=2, another=True)
        self.id_parent.grid(row=3, column=0, pady=5, padx=20, sticky='w')

        # Create the entry frame Telefono Representante
        self.phone_parent = EntryFrame(self.body_right, 450, 50,"Telefono", placeholder="Telefono Representante", layout=2)
        self.phone_parent.grid(row=4, column=0, pady=5, padx=20, sticky='w')

        #* ------------------------ Buttons frame

        # Create the button to add the parent
        self.add_parent_button = ctk.CTkButton(self.buttons_frame, width=100, height=34, text='Agregar', command=self.add_parent, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.add_parent_button.grid(row=0, column=0, pady=5, padx=20, sticky='n')

        # Create the button to eliminate the parent
        self.delete_parent_button = ctk.CTkButton(self.buttons_frame, width=100, height=34, text='Eliminar', command=self.delete_parent, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.delete_parent_button.grid(row=0, column=1, pady=5, padx=20, sticky='n')

        # center the buttons
        self.buttons_frame.grid_columnconfigure(0, weight=1)
        self.buttons_frame.grid_columnconfigure(1, weight=1)

        #* ------------------------ Footer
        # Create the Search bar
        self.search_bar = EntryFrame(self.footer, 500, 50,"Buscar", placeholder="Cedula Estudiante", layout=2, another=True)
        self.search_bar.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Create the button to add the student
        self.add_button = ctk.CTkButton(self.footer, width=100, height=34, text='Agregar', command=self.add_student, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.add_button.grid(row=0, column=3, pady=5, padx=20, sticky='s')

        # Create the button to save the student
        self.save_button = ctk.CTkButton(self.footer, width=100, height=34, text='Guardar', command=self.save_student, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.save_button.grid(row=0, column=2, pady=5, padx=20, sticky='s')

        # Create the button to delete the student
        self.delete_button = ctk.CTkButton(self.footer, width=100, height=34, text='Eliminar', command=self.delete_student, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.delete_button.grid(row=0, column=1, pady=5, padx=20, sticky='s')

        # Create the button to change view
        self.change_view_button = ctk.CTkButton(self.footer, width=100, height=34, text='Cambiar vista', command=self.change_view, font=('Arial', 15, 'bold'), bg_color='transparent', fg_color="#47959b", text_color='#ffffff', corner_radius=10)
        self.change_view_button.grid(row=0, column=4, pady=5, padx=20, sticky='s')


        #* ------------------------ Functions
    def change_grade(self):
        pass

    def add_parent(self):
        pass

    def delete_parent(self):
        pass

    def add_student(self):
        pass

    def save_student(self):
        pass

    def delete_student(self):
        pass

    def change_view(self):
        pass




#^===================================================Grades Layout
class GradesLayout(ctk.CTkFrame):
    '''Grades Layout'''
    pass



#^===================================================Schedule Layout
class ScheduleLayout(ctk.CTkFrame):
    '''Schedule Layout'''
    pass










#$------------------------ Main App
App=ctk.CTk()
App.title('Nibble') # Set the title of the app
App.iconbitmap('Nibble/recursos/logo/Nibble.ico') # Set the icon of the app
App.after(50, lambda: App.state('zoomed')) # Maximize the app
# App.minsize(900, 700) # Set the minimum size of the app
App.after(50, lambda: App.resizable(False,False)) # Minimize the app


#*------------------------ Img background from login section
img = ctk.CTkImage(Image.open('Nibble/recursos/background.jpg'), size=(1920,1080))
img_label = ctk.CTkLabel(App, image=img)
img_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#*------------------------ Background frame
background = ctk.CTkFrame(App, 720, 615, 50, fg_color='#eafbff', bg_color='transparent', background_corner_colors=['#a7bad6', '#b6c9e2', '#0b0c0e', '#070304'])
background.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#*------------------------ Login
# LoginLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
background.destroy()
new_background = ctk.CTkFrame(App, corner_radius=0, fg_color='#eafbff', bg_color='transparent')
new_background.place(relx=0, rely=0, relwidth=1, relheight=1)
AppLayout(new_background).place(relx=0, rely=0, relwidth=1, relheight=1)

#------------------------ Run the app
App.mainloop()
