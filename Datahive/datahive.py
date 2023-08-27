'''App for managing data from a School'''


import tkinter as ttk # Import the tkinter module
import customtkinter as ctk # Import the customtkinter module
from modules import Sections  # Import the Sections class from modules.py

app=ctk.CTk() # Create a new customtkinter app
app.title('Datahive') # Set the title of the app

app.geometry('720x615+514+108') # Set the size of the app
app.minsize(720, 615) # Set the minimum size of the app

header = Sections(app, 570, 100) # Create a the header section
header.place(x=150, y=0)

sidebar = Sections(app, 150, 515) # Create a the sidebar section
sidebar.place(x=0, y=0)

body = Sections(app, 570, 415) # Create a the body section
body.place(x=150, y=100)

footer = Sections(app, 720, 100) # Create a the footer section
footer.place(x=0, y=515)

app.mainloop()
