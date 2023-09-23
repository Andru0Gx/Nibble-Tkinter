'''App for managing data from a School'''


import tkinter as tk # Import the tkinter module
from tkinter import messagebox # Import the messagebox module
import datetime # Import the datetime module
import tkcalendar # Import the tkcalendar module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections, EntryFrame, ButtonFrame, button_frame # Import the Sections class from modules.py
from PIL import Image # Import the Image modules from PIL

#TODO - Sidebar con 2 layouts (pequeño y grande), el pequeño tiene los iconos y el grande tiene los textos + iconos
#TODO - Los credenciales hay que programarlos al final con la Base de datos

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
        fg_credentials = button_frame(self.body, text='Olvide mis credenciales.', command= self.loginto_forgot_credentials,hover=False, txcolor='#47959b')
        fg_credentials.grid(row=2, column=0, pady=0, padx=20 , sticky='w')

        #*----------------------------------------- footer widgets
        # Create the register button
        registrarse_button = button_frame(self.body, 'Registrarse', self.loginto_register, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        registrarse_button.grid(row=3, column=0, pady=25, padx=20 , sticky='w')

        # Create the login button
        self.credentials = {"user": "admin", "password": "1234"} # Credentials dictionary
        ingresar_button = button_frame(self.body, 'Ingresar', self.validate_entry, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
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
        options_frame = Sections(options, 400, 100)
        options_frame.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        # Create the buttons
        forgot_user = button_frame(options_frame, 'Usuario', lambda: select_option("user"), True, 'transparent', '#47959b', 28,100, font=('Arial', 15, 'bold'))
        forgot_user.grid(row=1, column=0, pady=5, padx=5 , sticky='w')

        forgot_password = button_frame(options_frame, 'Contraseña', lambda: select_option("password"), True, 'transparent', '#47959b', 28,100, font=('Arial', 15, 'bold'))
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
        registrarse_button = button_frame(self.footer, 'Registrarse', self.validate_entry, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
        registrarse_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    #*------------------------ Class Functions
    def validate_entry(self):
        '''Validate the entrys'''
        if self.user.entry.get() == '' or self.email.entry.get() == '' or self.password.entry.get() == '' or self.confirm_password.entry.get() == '' or self.security_answer1.entry.get() == '' or self.security_answer2.entry.get() == '' or self.security_answer3.entry.get() == '':
            messagebox.showerror('Campos Vacios', 'Por favor ingrese todos los datos')
        elif self.password.entry.get() != self.confirm_password.entry.get():
            messagebox.showerror('Contraseñas no coinciden', 'Las contraseñas no coinciden')
        else:
            # TODO - Save the data in the database
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
        self.header = Sections(self, 680, 100, fcolor='transparent', bcolor='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = Sections(self, 680, 400, fcolor='transparent', bcolor='transparent',radius=25,bdcolor='#d4d4d4',border_width=2)
        self.body.place(relx=0.5, rely=0.60, anchor=tk.S)

        # Create the footer frame
        self.footer = Sections(self, 680, 180, fcolor='transparent', bcolor='transparent')
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
        self.continue_button = button_frame(self.footer, 'Continuar', self.validate_entry, True, 'transparent', '#47959b', 35, font=('Arial', 15, 'bold'))
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
            self.body = Sections(self, 680, 400, fcolor='transparent', bcolor='transparent',radius=25,bdcolor='#d4d4d4',border_width=2)
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
        self.header = Sections(self, 680, 100, fcolor='transparent', bcolor='transparent')
        self.header.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create the body frame
        self.body = Sections(self, 680, 400, fcolor='transparent', bcolor='transparent')
        self.body.place(relx=0.5, rely=0.52, anchor=tk.CENTER)

        #*----------------------------------------- header widgets
        # Create the back button
        back_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/back.png'), size=(30,30))
        back_button = button_frame(self.header,"", lambda: back_to_login(self),True,'transparent','transparent',30,30,img= back_img)
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
        buttons_frame = Sections(self.body, 680, 300, fcolor='transparent', bcolor='transparent')
        buttons_frame.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Create the button Liceo
        liceo_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/highschool2.png'), size=(200,200))
        liceo_button = button_frame(buttons_frame,"", self.loginto_highschool_mode,True,'transparent','transparent',150,150,img= liceo_img)
        liceo_button.grid(row=0, column=0, pady=5, padx=20, sticky='w')

        # Create the button Colegio
        colegio_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/school2.png'), size=(200,200))
        colegio_button = button_frame(buttons_frame,"", self.loginto_school_mode,True,'transparent','transparent',150,150,img= colegio_img)
        colegio_button.grid(row=0, column=1, pady=5, padx=20, sticky='w')

            #*------------------------ Class Functions

    #*===================================================Loginto school mode
    def loginto_school_mode(self):
        '''Change the layout to mode selection'''
        img_label.destroy()
        self.destroy()
        background.configure(width=1536, height=793, corner_radius=0)
        school = AppLayout(background,HomeLayout)
        school.place(relx=0, rely=0, anchor=tk.NW)

    #*===================================================Loginto highschool mode
    def loginto_highschool_mode(self):
        '''Change the layout to mode selection'''
        img_label.destroy()
        self.destroy()
        background.configure(width=1536, height=793, corner_radius=0)




#^===================================================App Layout
class AppLayout(ctk.CTkFrame):
    '''Layout of the app'''
    def __init__(self, master, class_name):
        super().__init__(
            master = master,
            bg_color='#f5fdff',
            fg_color='#f5fdff',
            width=App.winfo_screenwidth(),
            height=App.winfo_screenheight(),
            )

        #* ------------------------ Frames
        # Create the header frame
        self.header = Sections(self, App.winfo_screenwidth(), 100, fcolor='#f5fdff', bcolor='#f5fdff')
        self.header.pack(side=tk.TOP)

        # Create the sidebar frame
        self.sidebar = Sections(self, 300, 693, fcolor='#f5fdff', bcolor='#f5fdff')
        self.sidebar.pack(side=tk.LEFT)

        # Create the body frame
        self.body = Sections(self, int(App.winfo_screenwidth())-299, 693, fcolor='#f5f5f5', bcolor='#f5fdff', bdcolor='#c2c9db', border_width=1.3)
        self.body.pack(side=tk.BOTTOM)

        #* ------------------------ Header
        # Header title
        self.title = ctk.CTkLabel(
            master = self.header,
            text = 'Grupo Escolar San Simon',
            font = ('Arial', 40, 'bold'),
            text_color='#243233',
            )
        self.title.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

        # Create the logo image and label
        logo_img = ctk.CTkImage(Image.open('Nibble/recursos/logo/Nibble-Logo-2.png'), size=(150,50))
        logo_label = ctk.CTkLabel(self.header, image=logo_img, corner_radius=50, text="", fg_color='#f5fdff', bg_color='#f5fdff')
        logo_label.place(relx=0.1, rely=0.5, anchor=tk.CENTER)


        #* ------------------------ Sidebar
        # --------------- Sidebar buttons
        # Home button
        home_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/home.png'), size=(50,50))
        home_button = ButtonFrame(self.sidebar,"Inicio",'transparent','transparent', lambda: print("home"),30,30,True,font=('Arial', 25), txcolor='#32464b',img= home_img, hover_color='#cdd8f5', layout=2)
        home_button.place(relx=0.5, rely=0.06, anchor=tk.CENTER)

        # Teachers button
        teachers_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/teachers.png'), size=(50,50))
        teachers_button = ButtonFrame(self.sidebar,"Profesores",command=lambda: print("teachers"),size_x=30,size_y=30,font=('Arial', 25), txcolor='#32464b',img= teachers_img, hover_color='#cdd8f5', layout=2)
        teachers_button.place(relx=0.5, rely=0.18, anchor=tk.CENTER)

        # Students button
        students_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/student.png'), size=(50,50))
        students_button = ButtonFrame(self.sidebar,"Estudiantes",command= lambda: print("students"),size_x=30,size_y=30,font=('Arial', 25), txcolor='#32464b',img= students_img, hover_color='#cdd8f5', layout=2)
        students_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        # Grades button
        grades_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/grades.png'), size=(50,50))
        grades_button = ButtonFrame(self.sidebar,"Notas",command=lambda: print("grades"),size_x=30,size_y=30,font=('Arial', 25), txcolor='#32464b',img= grades_img, hover_color='#cdd8f5', layout=2)
        grades_button.place(relx=0.5, rely=0.42, anchor=tk.CENTER)

        # Schedule button
        schedule_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/schedule.png'), size=(50,50))
        schedule_button = ButtonFrame(self.sidebar,"Horario",command=lambda: print("schedule"),size_x=30,size_y=30,font=('Arial', 25), txcolor='#32464b',img= schedule_img, hover_color='#cdd8f5', layout=2)
        schedule_button.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

        # Change Mode button
        change_mode_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/change_mode_dark.png'), size=(50,50))
        change_mode_button = ButtonFrame(self.sidebar,"Cambiar modo",command=lambda: print("change mode"),size_x=30,size_y=30,font=('Arial', 25), txcolor='#32464b',img= change_mode_img, hover_color='#cdd8f5', layout=3)
        change_mode_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


        #* ------------------------ Body
        class_name(self.body).place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#^===================================================Home Layout
class HomeLayout(ctk.CTkFrame):
    '''Home Layout (Calendar, identifier label)'''
    def __init__(self, master):
        super().__init__(
            master = master,
            bg_color='transparent',
            fg_color='transparent',
            width=1230,
            height=690,
        )

        #* ------------------------ Frames
        # Create the calendar frame
        self.body = Sections(self, 1230, 690, fcolor='transparent', bcolor='transparent')
        self.body.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        #* ------------------------ Calendar
        # Create the calendar
        self.calendar = tkcalendar.Calendar(self.body, font=('Arial', 15), selectmode='day', locale='es_ES', date_pattern='dd/mm/yyyy')
        self.calendar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # increase the size of the calendar
        self.calendar.bind('<Enter>', lambda event: self.calendar.place_configure(width=1230, height=690))

        # Create events on the calendar
        self.calendar.calevent_create(datetime.datetime(2023,9,25), 'Inicio de clases', 'school')













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
LoginLayout(background).place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#------------------------ Run the app
App.mainloop()
