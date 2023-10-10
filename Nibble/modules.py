'''Modules of the app'''
import customtkinter as ctk # Import the customtkinter module
import datetime # Import the datetime module
from PIL import Image # Import the Image module


#$ ------------------------ Classes

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
            if layout == 1: # If layout is 0, place the label and the entry in the frame
                self.entry.configure(width = int (size_x/1.13)) # Change the width of the entry
                self.button.grid(row=1, column=1, pady=5, padx=3, sticky='w') # Place the button
            elif layout == 2: # If layout is 1, place the label and the entry in the frame
                self.button.grid(row=0, column=2, pady=5, padx=3, sticky='w') # Place the button


        if layout == 1: # If layout is 0, place the label and the entry in the frame
            self.label.grid(row=0, column=0, pady=5, padx=0, sticky='w')
            self.entry.grid(row=1, column=0, pady=5, padx=0 , sticky='w')
        elif layout == 2: # If layout is 1, place the label and the entry in the frame
            self.label.grid(row=0, column=0, pady=5, padx=10, sticky='w')
            self.entry.grid(row=0, column=1, pady=5, padx=10 , sticky='w')


# Create the Button frames for the app
class ButtonFrame(ctk.CTkFrame):
    '''Button frames of the sidebar'''
    def __init__(self,master,text,bcolor = 'transparent',fcolor = 'transparent',command = None,size_y = 28,size_x = 140, hover = True, font = None ,txcolor = None,img = None,cradius = None,hover_color = '#47959b', layout = 1):
        super().__init__(
                master = master,
                bg_color='transparent',
                fg_color='transparent',
                height= 80,
                width= 280,
            )
        self.button = ctk.CTkButton(
            master = self,
            text = text,
            bg_color = bcolor,
            fg_color = fcolor,
            hover=hover,
            height= size_y,
            width= size_x,
            command = command,
            text_color=txcolor,
            font=font,
            image=img,
            corner_radius= cradius,
            hover_color=hover_color,
            )

        if layout == 1:
            self.button.place(relx=0.5, rely=0.5, anchor='center')
            self.configure(height= 35, width= 140)
        elif layout == 2:
            self.button.place(relx=0.5, rely=0.4, anchor='center')
            separator = ctk.CTkLabel(self, text="", bg_color='#cdd4f0', fg_color='#cdd4f0')
            separator.place(relx=0.5, rely=0.85, anchor='center', relwidth=0.7, relheight=0.015)
        elif layout == 3:
            self.button.place(relx=0.5, rely=0.6, anchor='center')
            separator = ctk.CTkLabel(self, text="", bg_color='#cdd4f0', fg_color='#cdd4f0')
            separator.place(relx=0.5, rely=0.15, anchor='center', relwidth=0.7, relheight=0.015)

class EventsFrame(ctk.CTkFrame):
    '''Events frames of the calendar'''
    def __init__(self, master, event_tittle, event_description, event_date, calendar_name, window_name, function_name):
        super().__init__(
                master = master,
                bg_color='transparent',
                fg_color='transparent',
                height= 35,
                width= 760,
            )
        size_description = 1
        size_tittle = 1
        new_event_tittle = event_tittle
        new_event_description = event_description

        # if the description is too long, start a new line
        if len(event_description) > 13:
            for i in range(13,len(event_description),13):
                new_event_description = new_event_description[:i] + '\n' + new_event_description[i:]
                size_description += 1

        # if the tittle is too long, start a new line
        if len(event_tittle) > 13:
            for i in range(13,len(event_tittle),13):
                new_event_tittle = new_event_tittle[:i] + '\n' + new_event_tittle[i:]
                size_tittle += 1
        # Create the event Widgets
        # Event title
        self.tittle = ctk.CTkLabel(self, text=new_event_tittle, font=('Arial', 15, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.tittle.place(relx=0.1, rely=0.5, anchor='center')

        # Event description
        self.description = ctk.CTkLabel(self, text=new_event_description, font=('Arial', 15, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.description.place(relx=0.4, rely=0.5, anchor='center')

        # Event date
        self.date = ctk.CTkLabel(self, text=event_date.strftime("%d / %m / %Y"), font=('Arial', 15, "bold"), bg_color='transparent', fg_color=None,text_color='#243233')
        self.date.place(relx=0.7, rely=0.5, anchor='center')

        # Edit event button
        edit_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/edit.png'), size= (20, 20))
        self.edit_button = ctk.CTkButton(self,width=25, height=29 ,text='', command= lambda: self.edit_event(calendar_name,event_date,window_name, function_name, event_description), bg_color='transparent', fg_color="#47959b", corner_radius=10, image=edit_img)
        self.edit_button.place(relx=0.87, rely=0.5, anchor='center')

        # Delete event button
        delete_img = ctk.CTkImage(Image.open('Nibble/recursos/icons/delete.png'), size= (20, 20))
        self.delete_button = ctk.CTkButton(self,width=25, height=29,text="" ,command= lambda: self.delete_event(calendar_name,event_date), bg_color='transparent', fg_color="#fa4541", corner_radius=10, image=delete_img)
        self.delete_button.place(relx=0.935, rely=0.5, anchor='center')

        # Change the size of the frame
        if size_description > size_tittle and size_description > 1:
            self.description.configure(height= 20*size_description)
            # aumentar el tamaño del frame
            self.configure(height= 22*size_description)

        elif size_tittle > size_description and size_tittle > 1:
            self.tittle.configure(height= 20*size_tittle)
            # aumentar el tamaño del frame
            self.configure(height= 22*size_tittle)


    def delete_event(self, calendar, date):
        '''Delete the event from the calendar'''
        id_event = calendar.get_calevents(date)
        calendar.calevent_remove(id_event[0])
        self.destroy()

    def update_event(self, function, calendar, date, window):
        '''Update the event from the calendar'''
        name = window.event_name.entry.get()
        description = window.description.entry.get()
        self.delete_event(calendar, date)
        function(name, description)

    def edit_event(self, calendar, date, window, function, tag):
        '''Edit the event from the calendar'''
        # Get the event date
        dates = str(self.date.cget('text'))
        dates = dates.split(' / ')
        date = datetime.date(int(dates[2]), int(dates[1]), int(dates[0]))

        # Get the event tag
        tags = str(self.description.cget('text'))
        tags = tags.replace('\n', ' ').replace('[', '').replace(']', '').replace("'", '').split(' ')
        tag = tags[0]

        # Get the event data
        id_event = calendar.get_calevents(date, tag)
        text = calendar.calevent_cget(id_event[0], 'text')
        tag = calendar.calevent_cget(id_event[0], 'tags')

        # Activate the date entry
        window.date_entry.entry.configure(state='normal')

        # Delete the entrys
        if window.event_name.entry.cget != '':
            window.event_name.entry.delete(0, 'end')
            window.date_entry.entry.delete(0, 'end')
            window.description.entry.delete(0, 'end')

        # Insert the event data
        window.event_name.entry.insert(0, text)
        window.date_entry.entry.insert(0, date.strftime("%d / %m / %Y"))
        window.description.entry.insert(0, tag)

        # Deactivate the date entry
        window.date_entry.entry.configure(state='readonly')

        window.event_button.configure(text = 'Guardar', command=lambda: self.update_event(function, calendar, date, window))
