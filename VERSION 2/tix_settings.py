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

        # Series of functions for the text value below each slider
        def update_gd1(value):
            self.gd1.config(text=value)
            # Dynamic positioning formula
            self.gd1.place(x=170 - (len(value) - 1) * 5, y=400) 

        def update_gd2(value):
            self.gd2.config(text=value)
            self.gd2.place(x=170 - (len(value) - 1) * 5, y=560)

        def update_ed1(value):
            self.ed1.config(text=value)
            self.ed1.place(x=480 - (len(value) - 1) * 5, y=400)

        def update_ed2(value):
            self.ed2.config(text=value)
            self.ed2.place(x=480 - (len(value) - 1) * 5, y=560)

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

        # Placing save button
        self.save = tk.PhotoImage(file="Designs/Settings/Save_Button.png")
        self.save_button = tk.Button(self.root, image=self.save, relief="raised")
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
            to=45, 
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
        self.gd1 = tk.Label(root, text=self.glinda_day_one_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.gd1.place(x=170, y=400)

        # Placing slider for Glinda - Day 2
        self.glinda_day_two_seats = Scale(
            self.root, 
            from_=1,
            to=45, 
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
        self.gd2 = tk.Label(root, text=self.glinda_day_two_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.gd2.place(x=170, y=560)

        # Placing slider for Elphaba - Day 1
        self.elphaba_day_one_seats = Scale(
            self.root, 
            from_=1,
            to=45, 
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
        self.ed1 = tk.Label(root, text=self.elphaba_day_one_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.ed1.place(x=480, y=400)

        # Placing slider for Elphaba - Day 2
        self.elphaba_day_two_seats = Scale(
            self.root, 
            from_=1,
            to=45, 
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
        self.ed2 = tk.Label(root, text=self.elphaba_day_two_seats.get(), bd=1, font="Helvetica", bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.ed2.place(x=480, y=560)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = TixSettings(root)
    root.mainloop()