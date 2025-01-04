# Importing necessary libraries
from tkinter import *
import tkinter as tk

# Main class for settings page
class TixSettings:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Tix Master - Settings")
        self.root.configure(bg="#d9e2f1")

        # Initializing settings dictionary variable
        self.settings_list = {}

        # Series of functions for the text value below each slider
        def update_gd1(value):
            self.gd1.config(text=value)
            self.gd1.place(x=170 - (len(value) - 1) * 5, y=400)
            self.check_sold_out()

        def update_gd2(value):
            self.gd2.config(text=value)
            self.gd2.place(x=170 - (len(value) - 1) * 5, y=560)
            self.check_sold_out()

        def update_ed1(value):
            self.ed1.config(text=value)
            self.ed1.place(x=480 - (len(value) - 1) * 5, y=400)
            self.check_sold_out()

        def update_ed2(value):
            self.ed2.config(text=value)
            self.ed2.place(x=480 - (len(value) - 1) * 5, y=560)
            self.check_sold_out()

        # Placing the main design of the catalogue page
        self.settings_title = tk.PhotoImage(file="Designs/Settings/Tix_Settings.png")
        self.settings_title_label = tk.Label(self.root, image=self.settings_title, bg="#d9e2f1")
        self.settings_title_label.image = self.settings_title
        self.settings_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing reserve ticket button
        self.reserve = tk.PhotoImage(file="Designs/Settings/Reserve.png")
        self.reserve_button = tk.Button(self.root, image=self.reserve, relief="raised")
        self.reserve_button.image = self.reserve
        self.reserve_button.place(x=809, y=425, anchor="center")
        self.reserve_hover = tk.PhotoImage(file="Designs/Settings/Reserve_Hover.png")
        self.reserve_button.bind("<Enter>", self.on_hover_reserve)
        self.reserve_button.bind("<Leave>", self.on_leave_reserve)
        self.reserve_button.image = self.reserve_hover

        # Placing view history button
        self.view_history = tk.PhotoImage(file="Designs/Settings/View_History.png")
        self.view_history_button = tk.Button(self.root, image=self.view_history, relief="raised")
        self.view_history_button.image = self.view_history
        self.view_history_button.place(x=809, y=525, anchor="center")
        self.view_history_hover = tk.PhotoImage(file="Designs/Settings/View_History_Hover.png")
        self.view_history_button.bind("<Enter>", self.on_hover_view_history)
        self.view_history_button.bind("<Leave>", self.on_leave_view_history)
        self.view_history_button.image = self.view_history_hover

        # Placing save button
        self.save = tk.PhotoImage(file="Designs/Settings/Save_Button.png")
        self.save_button = tk.Button(self.root, image=self.save, relief="raised", command=self.save_settings) # Call function to collect all settings 
        self.save_button.image = self.save
        self.save_button.place(x=720, y=625, anchor="center")
        self.save_hover = tk.PhotoImage(file="Designs/Settings/Save_Button_Hover.png")
        self.save_button.bind("<Enter>", self.on_hover_save)
        self.save_button.bind("<Leave>", self.on_leave_save)
        self.save_button.image = self.save_hover

        # Placing return button
        self.back = tk.PhotoImage(file="Designs/Settings/Back_Button.png")
        self.back_button = tk.Button(self.root, image=self.back, relief="raised", command=self.open_title) # Call function that opens main menu
        self.back_button.image = self.back
        self.back_button.place(x=895, y=625, anchor="center")
        self.back_hover = tk.PhotoImage(file="Designs/Settings/Back_Button_Hover.png")
        self.back_button.bind("<Enter>", self.on_hover_back)
        self.back_button.bind("<Leave>", self.on_leave_back)
        self.back_button.image = self.back_hover

        # Placing slider for Glinda - Day 1
        self.glinda_day_one_seats = Scale(
            # Bunch of documentation for this because there's so many settings
            self.root, 
            from_=1, # Interval of the slider
            to=43, 
            orient=HORIZONTAL, # Orientation
            length=200, # Length and width 
            width=20, 
            showvalue=False, # Hide the labels 
            bg="#798ec4", # Color of the square you drag
            highlightthickness=0, # Remove ugly border
            troughcolor="#ccd9f3", # Color of the background 
            relief="sunken", # Relief of the background
            activebackground="#798ec4", # Did this to avoid sudden color change when hovering the square
            sliderrelief="ridge", # Relief of the square
            command=update_gd1
        )
        self.glinda_day_one_seats.place(x=170, y=380, anchor="center") # Positioning

        # Placing label value for Glinda - Day 1
        self.gd1 = tk.Label(self.root, text=self.glinda_day_one_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.gd1.place(x=170, y=400)

        # Placing slider for Glinda - Day 2
        self.glinda_day_two_seats = Scale(
            self.root, 
            from_=1,
            to=43, 
            orient=HORIZONTAL, 
            length=200, 
            width=20, 
            showvalue=False, 
            bg="#798ec4", 
            highlightthickness=0,
            troughcolor="#ccd9f3", 
            relief="sunken",
            activebackground="#798ec4", 
            sliderrelief="ridge",
            command=update_gd2
        )
        self.glinda_day_two_seats.place(x=170, y=540, anchor="center")

        # Placing label value for Glinda - Day 2
        self.gd2 = tk.Label(self.root, text=self.glinda_day_two_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.gd2.place(x=170, y=560)

        # Placing slider for Elphaba - Day 1
        self.elphaba_day_one_seats = Scale(
            self.root, 
            from_=1,
            to=43, 
            orient=HORIZONTAL, 
            length=200, 
            width=20, 
            showvalue=False, 
            bg="#798ec4", 
            highlightthickness=0,
            troughcolor="#ccd9f3", 
            relief="sunken",
            activebackground="#798ec4", 
            sliderrelief="ridge",
            command=update_ed1
        )
        self.elphaba_day_one_seats.place(x=480, y=380, anchor="center")

        # Placing label value for Elphaba - Day 1
        self.ed1 = tk.Label(self.root, text=self.elphaba_day_one_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.ed1.place(x=480, y=400)

        # Placing slider for Elphaba - Day 2
        self.elphaba_day_two_seats = Scale(
            self.root, 
            from_=1,
            to=43, 
            orient=HORIZONTAL, 
            length=200, 
            width=20, 
            showvalue=False, 
            bg="#798ec4", 
            highlightthickness=0,
            troughcolor="#ccd9f3", 
            relief="sunken",
            activebackground="#798ec4", 
            sliderrelief="ridge",
            command=update_ed2
        )
        self.elphaba_day_two_seats.place(x=480, y=540, anchor="center")

        # Placing label value for Elphaba - Day 2
        self.ed2 = tk.Label(self.root, text=self.elphaba_day_two_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.ed2.place(x=480, y=560)

        # Series of checkbox buttons for the sold out feature
        self.gd1_value = tk.IntVar()
        self.gd1_check = tk.Checkbutton(self.root, text="Glinda Day 1", variable=self.gd1_value, onvalue=1, offvalue=0, relief="ridge", bg="#798ec4", activebackground="#798ec4", fg="#d9e2f1", activeforeground="#d9e2f1", disabledforeground="#d9e2f1", selectcolor="#798ec4", command=self.update_gd1_check)
        self.gd1_check.config(width=12, font=("Helvetica", 10, "bold"))
        self.gd1_check.place(x=668, y=275)

        self.gd2_value = tk.IntVar()
        self.gd2_check = tk.Checkbutton(self.root, text="Glinda Day 2", variable=self.gd2_value, onvalue=1, offvalue=0, relief="ridge", bg="#798ec4", activebackground="#798ec4", fg="#d9e2f1", activeforeground="#d9e2f1", disabledforeground="#d9e2f1", selectcolor="#798ec4", command=self.update_gd2_check)
        self.gd2_check.config(width=12, font=("Helvetica", 10, "bold"))
        self.gd2_check.place(x=668, y=315)

        self.ed1_value = tk.IntVar()
        self.ed1_check = tk.Checkbutton(self.root, text="Elphaba Day 1", variable=self.ed1_value, onvalue=1, offvalue=0, relief="ridge", bg="#798ec4", activebackground="#798ec4", fg="#d9e2f1", activeforeground="#d9e2f1", disabledforeground="#d9e2f1", selectcolor="#798ec4", command=self.update_ed1_check)
        self.ed1_check.config(width=12, font=("Helvetica", 10, "bold"))
        self.ed1_check.place(x=823, y=275)

        self.ed2_value = tk.IntVar()
        self.ed2_check = tk.Checkbutton(self.root, text="Elphaba Day 2", variable=self.ed2_value, onvalue=1, offvalue=0, relief="ridge", bg="#798ec4", activebackground="#798ec4", fg="#d9e2f1", activeforeground="#d9e2f1", disabledforeground="#d9e2f1", selectcolor="#798ec4", command=self.update_ed2_check)
        self.ed2_check.config(width=12, font=("Helvetica", 10, "bold"))
        self.ed2_check.place(x=823, y=315)

        # Loading the settings upon startup 
        self.load_settings()

        # Check and disable concerts if slider value reaches maximum
        self.check_sold_out()

    # Series of functions for the hover effects for each button
    def on_hover_reserve(self, event):
        self.reserve_button.config(image=self.reserve_hover)

    def on_leave_reserve(self, event):
        self.reserve_button.config(image=self.reserve)

    def on_hover_view_history(self, event):
        self.view_history_button.config(image=self.view_history_hover)

    def on_leave_view_history(self, event):
        self.view_history_button.config(image=self.view_history)

    def on_hover_save(self, event):
        self.save_button.config(image=self.save_hover)

    def on_leave_save(self, event):
        self.save_button.config(image=self.save)

    def on_hover_back(self, event):
        self.back_button.config(image=self.back_hover)

    def on_leave_back(self, event):
        self.back_button.config(image=self.back)

    # Function for opening the main menu
    def open_title(self):
        from tix_master import TixMaster
        self.settings_title_label.place_forget()
        TixMaster(self.root)

    # Function for opening the save message
    def open_save(self):
        from save_message import Save
        save_window = tk.Toplevel(self.root)
        Save(save_window)

    # Function for collecting all current settings  - activates when save button is clicked
    def save_settings(self):
        # Store all the settings in a dictionary
        self.settings_list = {
            'is_sold_out_gd1': self.gd1_value.get(), # Using get command to get the values of tkinter stuff
            'is_sold_out_gd2': self.gd2_value.get(),
            'is_sold_out_ed1': self.ed1_value.get(),
            'is_sold_out_ed2': self.ed2_value.get(),
            'queue_num_gd1': self.glinda_day_one_seats.get(),
            'queue_num_gd2': self.glinda_day_two_seats.get(),
            'queue_num_ed1': self.elphaba_day_one_seats.get(),
            'queue_num_ed2': self.elphaba_day_two_seats.get()
        }
        
        # Use file to write and loops through all the items in the dictionary
        with open("simulation_settings.dat", "w") as saveSettings:
            for key, value in self.settings_list.items():
                saveSettings.write(f"{key}:{value}\n")

        self.open_save() # Call function that opens the save message

    # Function for loading the settings whenever settings page is opened
    def load_settings(self):
        with open("simulation_settings.dat", "r") as loadSettings:
            load = loadSettings.readlines() # Convert text in the file to a string

            # Looping every line in the converted text and stores it to a variable to take the saved settings
            for num, line in enumerate(load):
                line = line.strip()  
                if num == 0:
                    is_sold_out_gd1 = int(line.split(':')[1]) # Splits each line into two and takes the latter half (right side of semicolon) as it contains the values
                elif num == 1:
                    is_sold_out_gd2 = int(line.split(':')[1])
                elif num == 2:
                    is_sold_out_ed1 = int(line.split(':')[1])
                elif num == 3:
                    is_sold_out_ed2 = int(line.split(':')[1])
                elif num == 4:
                    queue_num_gd1 = int(line.split(':')[1])
                elif num == 5:
                    queue_num_gd2 = int(line.split(':')[1])
                elif num == 6:
                    queue_num_ed1 = int(line.split(':')[1])
                elif num == 7:
                    queue_num_ed2 = int(line.split(':')[1])

            # Setting the checkbox and sliders to the values taken from these above
            self.gd1_value.set(is_sold_out_gd1)
            self.gd2_value.set(is_sold_out_gd2)
            self.ed1_value.set(is_sold_out_ed1)
            self.ed2_value.set(is_sold_out_ed2)
            self.glinda_day_one_seats.set(queue_num_gd1)
            self.glinda_day_two_seats.set(queue_num_gd2)
            self.elphaba_day_one_seats.set(queue_num_ed1)
            self.elphaba_day_two_seats.set(queue_num_ed2)

        # Check and disable concerts if slider value reaches maximum
        self.check_sold_out()

    # Function to update checkbox state based on slider value
    def update_gd1_check(self):
        if self.gd1_value.get() == 1: # If checkbox is ticked, automatically set the slider to 43
            self.glinda_day_one_seats.set(43)
        else:
            self.glinda_day_one_seats.set(1)

    def update_gd2_check(self):
        if self.gd2_value.get() == 1:
            self.glinda_day_two_seats.set(43)
        else:
            self.glinda_day_two_seats.set(1)

    def update_ed1_check(self):
        if self.ed1_value.get() == 1:
            self.elphaba_day_one_seats.set(43)
        else:
            self.elphaba_day_one_seats.set(1)

    def update_ed2_check(self):
        if self.ed2_value.get() == 1:
            self.elphaba_day_two_seats.set(43)
        else:
            self.elphaba_day_two_seats.set(1)

    # Function to check and disable concerts if slider value reaches 43
    def check_sold_out(self):
        # This section is if the slider is maxed, it will tick the checkbox
        if self.glinda_day_one_seats.get() == 43:
            self.gd1_check.select()
        else:
            self.gd1_check.deselect()

        if self.glinda_day_two_seats.get() == 43:
            self.gd2_check.select()
        else:
            self.gd2_check.deselect()

        if self.elphaba_day_one_seats.get() == 43:
            self.ed1_check.select()
        else:
            self.ed1_check.deselect()

        if self.elphaba_day_two_seats.get() == 43:
            self.ed2_check.select()
        else:
            self.ed2_check.deselect()

        # While this section is for the checkbox, it will automatically max the slider
        if self.gd1_value.get() == 1:
            self.glinda_day_one_seats.set(43)

        if self.gd2_value.get() == 1:
            self.glinda_day_two_seats.set(43)

        if self.ed1_value.get() == 1:
            self.elphaba_day_one_seats.set(43)
            
        if self.ed2_value.get() == 1:
            self.elphaba_day_two_seats.set(43)

if __name__ == "__main__":
    root = tk.Tk()
    app = TixSettings(root)
    root.mainloop()