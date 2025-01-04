# Importing necessary libraries
import tkinter as tk

# Main class for concert options page
class ConcertCatalogue:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Tix Master - Concert Catalogue")
        self.root.configure(bg="#d9e2f1")

        # Initializing some variables for checking sold out status
        self.is_sold_out_gd1 = 0
        self.is_sold_out_gd2 = 0
        self.is_sold_out_ed1 = 0
        self.is_sold_out_ed2 = 0

        # Placing the main design of the catalogue page
        self.catalogue_title = tk.PhotoImage(file="Designs/Catalogue/Concert_Catalogue.png")
        self.catalogue_title_label = tk.Label(self.root, image=self.catalogue_title, bg="#d9e2f1")
        self.catalogue_title_label.image = self.catalogue_title
        self.catalogue_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing Glinda - Day 1 button
        self.glinda_day_one = tk.PhotoImage(file="Designs/Catalogue/Glinda_Day_One.png")
        self.glinda_day_one_button = tk.Button(self.root, image=self.glinda_day_one, relief="raised", command=self.open_loading)
        self.glinda_day_one_button.image = self.glinda_day_one
        self.glinda_day_one_button.place(x=195, y=575, anchor="center")
        self.glinda_day_one_hover = tk.PhotoImage(file="Designs/Catalogue/Glinda_Day_One_Hover.png")
        self.glinda_day_one_button.bind("<Enter>", self.on_hover_glinda_one)
        self.glinda_day_one_button.bind("<Leave>", self.on_leave_glinda_one)
        self.glinda_day_one_button.image = self.glinda_day_one_hover
        self.glinda_day_one_sold = tk.PhotoImage(file="Designs/Catalogue/GD1_Sold_Out.png")

        # Placing Glinda - Day 2 button
        self.glinda_day_two = tk.PhotoImage(file="Designs/Catalogue/Glinda_Day_Two.png")
        self.glinda_day_two_button = tk.Button(self.root, image=self.glinda_day_two, relief="raised", command=self.open_loading)
        self.glinda_day_two_button.image = self.glinda_day_two
        self.glinda_day_two_button.place(x=375, y=575, anchor="center")
        self.glinda_day_two_hover = tk.PhotoImage(file="Designs/Catalogue/Glinda_Day_Two_Hover.png")
        self.glinda_day_two_button.bind("<Enter>", self.on_hover_glinda_two)
        self.glinda_day_two_button.bind("<Leave>", self.on_leave_glinda_two)
        self.glinda_day_two_button.image = self.glinda_day_two_hover
        self.glinda_day_two_sold = tk.PhotoImage(file="Designs/Catalogue/GD2_Sold_Out.png")

        # Placing Elphaba - Day 1 button
        self.elphaba_day_one = tk.PhotoImage(file="Designs/Catalogue/Elphaba_Day_One.png")
        self.elphaba_day_one_button = tk.Button(self.root, image=self.elphaba_day_one, relief="raised", command=self.open_loading)
        self.elphaba_day_one_button.image = self.elphaba_day_one
        self.elphaba_day_one_button.place(x=625, y=575, anchor="center")
        self.elphaba_day_one_hover = tk.PhotoImage(file="Designs/Catalogue/Elphaba_Day_One_Hover.png")
        self.elphaba_day_one_button.bind("<Enter>", self.on_hover_elphaba_one)
        self.elphaba_day_one_button.bind("<Leave>", self.on_leave_elphaba_one)
        self.elphaba_day_one_button.image = self.elphaba_day_one_hover
        self.elphaba_day_one_sold = tk.PhotoImage(file="Designs/Catalogue/ED1_Sold_Out.png")

        # Placing Elphaba - Day 2 button
        self.elphaba_day_two = tk.PhotoImage(file="Designs/Catalogue/Elphaba_Day_Two.png")
        self.elphaba_day_two_button = tk.Button(self.root, image=self.elphaba_day_two, relief="raised", command=self.open_loading)
        self.elphaba_day_two_button.image = self.elphaba_day_two
        self.elphaba_day_two_button.place(x=805, y=575, anchor="center")
        self.elphaba_day_two_hover = tk.PhotoImage(file="Designs/Catalogue/Elphaba_Day_Two_Hover.png")
        self.elphaba_day_two_button.bind("<Enter>", self.on_hover_elphaba_two)
        self.elphaba_day_two_button.bind("<Leave>", self.on_leave_elphaba_two)
        self.elphaba_day_two_button.image = self.elphaba_day_two_hover
        self.elphaba_day_two_sold = tk.PhotoImage(file="Designs/Catalogue/ED2_Sold_Out.png")

        # Placing return button
        self.go_back = tk.PhotoImage(file="Designs/Catalogue/Catalogue_Back.png")
        self.go_back_button = tk.Button(self.root, image=self.go_back, relief="raised", command=self.open_title) # Call function that opens main menu
        self.go_back_button.image = self.go_back
        self.go_back_button.place(x=850, y= 630)
        self.go_back_hover = tk.PhotoImage(file="Designs/Catalogue/Catalogue_Back_Hover.png")
        self.go_back_button.bind("<Enter>", self.on_hover_back)
        self.go_back_button.bind("<Leave>", self.on_leave_back)
        self.go_back_button.image = self.go_back_hover

        # Loading the settings upon startup 
        self.load_settings()
        self.sold_out()

    # Series of functions for the hover effects for each button
    def on_hover_glinda_one(self, event):
        if self.is_sold_out_gd1 == 0:
            self.glinda_day_one_button.config(image=self.glinda_day_one_hover)

    def on_leave_glinda_one(self, event):
        if self.is_sold_out_gd1 == 0:
            self.glinda_day_one_button.config(image=self.glinda_day_one)

    def on_hover_glinda_two(self, event):
        if self.is_sold_out_gd2 == 0:
            self.glinda_day_two_button.config(image=self.glinda_day_two_hover)

    def on_leave_glinda_two(self, event):
        if self.is_sold_out_gd2 == 0:
            self.glinda_day_two_button.config(image=self.glinda_day_two)

    def on_hover_elphaba_one(self, event):
        if self.is_sold_out_ed1 == 0:
            self.elphaba_day_one_button.config(image=self.elphaba_day_one_hover)
    
    def on_leave_elphaba_one(self, event):
        if self.is_sold_out_ed1 == 0:
            self.elphaba_day_one_button.config(image=self.elphaba_day_one)

    def on_hover_elphaba_two(self, event):
        if self.is_sold_out_ed2 == 0:
            self.elphaba_day_two_button.config(image=self.elphaba_day_two_hover)

    def on_leave_elphaba_two(self, event):
        if self.is_sold_out_ed2 == 0:
            self.elphaba_day_two_button.config(image=self.elphaba_day_two)

    def on_hover_back(self, event):
        self.go_back_button.config(image=self.go_back_hover)
    
    def on_leave_back(self, event):
        self.go_back_button.config(image=self.go_back)

    # Function for going to the loading screens
    def open_loading(self):
        from tix_loading import TixLoading
        self.catalogue_title_label.place_forget()
        TixLoading(self.root)

    # Function for loading the settings whenever settings page is opened
    def load_settings(self):
        with open("simulation_settings.dat", "r") as loadSettings:
            load = loadSettings.readlines() # Convert text in the file to a string

            # Looping every line in the converted text and stores it to a variable to take the saved settings
            for num, line in enumerate(load):
                line = line.strip()  
                if num == 0:
                    self.is_sold_out_gd1 = int(line.split(':')[1]) # Splits each line into two and takes the latter half (right side of semicolon) as it contains the values
                elif num == 1:
                    self.is_sold_out_gd2 = int(line.split(':')[1])
                elif num == 2:
                    self.is_sold_out_ed1 = int(line.split(':')[1])
                elif num == 3:
                    self.is_sold_out_ed2 = int(line.split(':')[1])

    # Function for disabling buttons with sold out status
    def sold_out(self):
        if self.is_sold_out_gd1 == 1:
            self.glinda_day_one_button.config(image=self.glinda_day_one_sold, relief="sunken", command=self.open_sold_out)

        if self.is_sold_out_gd2 == 1:
            self.glinda_day_two_button.config(image=self.glinda_day_two_sold, relief="sunken", command=self.open_sold_out)

        if self.is_sold_out_ed1 == 1:
            self.elphaba_day_one_button.config(image=self.elphaba_day_one_sold, relief="sunken", command=self.open_sold_out)

        if self.is_sold_out_ed2 == 1:
            self.elphaba_day_two_button.config(image=self.elphaba_day_two_sold, relief="sunken", command=self.open_sold_out)

    # Function for opening the main menu
    def open_title(self):
        from tix_master import TixMaster
        self.catalogue_title_label.place_forget()
        TixMaster(self.root)

    # Function for opening the sold out message
    def open_sold_out(self):
        from sold_out_message import SoldOut
        sold_out_message = tk.Toplevel(self.root)
        SoldOut(sold_out_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcertCatalogue(root)
    root.mainloop()