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

        # Placing the main design of the catalogue page
        self.catalogue_title = tk.PhotoImage(file="Designs/Concert_Catalogue.png")
        self.catalogue_title_label = tk.Label(self.root, image=self.catalogue_title, bg="#d9e2f1")
        self.catalogue_title_label.image = self.catalogue_title
        self.catalogue_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing Glinda - Day 1 button
        self.glinda_day_one = tk.PhotoImage(file="Designs/Glinda_Day_One.png")
        self.glinda_day_one_button = tk.Button(self.root, image=self.glinda_day_one, relief="raised")
        self.glinda_day_one_button.image = self.glinda_day_one
        self.glinda_day_one_button.place(x=195, y=575, anchor="center")
        self.glinda_day_one_hover = tk.PhotoImage(file="Designs/Glinda_Day_One_Hover.png")
        self.glinda_day_one_button.bind("<Enter>", self.on_hover_glinda_one)
        self.glinda_day_one_button.bind("<Leave>", self.on_leave_glinda_one)
        self.glinda_day_one_button.image = self.glinda_day_one_hover

        # Placing Glinda - Day 2 button
        self.glinda_day_two = tk.PhotoImage(file="Designs/Glinda_Day_Two.png")
        self.glinda_day_two_button = tk.Button(self.root, image=self.glinda_day_two, relief="raised")
        self.glinda_day_two_button.image = self.glinda_day_two
        self.glinda_day_two_button.place(x=375, y=575, anchor="center")
        self.glinda_day_two_hover = tk.PhotoImage(file="Designs/Glinda_Day_Two_Hover.png")
        self.glinda_day_two_button.bind("<Enter>", self.on_hover_glinda_two)
        self.glinda_day_two_button.bind("<Leave>", self.on_leave_glinda_two)
        self.glinda_day_two_button.image = self.glinda_day_two_hover

        # Placing Elphaba - Day 1 button
        self.elphaba_day_one = tk.PhotoImage(file="Designs/Elphaba_Day_One.png")
        self.elphaba_day_one_button = tk.Button(self.root, image=self.elphaba_day_one, relief="raised")
        self.elphaba_day_one_button.image = self.elphaba_day_one
        self.elphaba_day_one_button.place(x=625, y=575, anchor="center")
        self.elphaba_day_one_hover = tk.PhotoImage(file="Designs/Elphaba_Day_One_Hover.png")
        self.elphaba_day_one_button.bind("<Enter>", self.on_hover_elphaba_one)
        self.elphaba_day_one_button.bind("<Leave>", self.on_leave_elphaba_one)
        self.elphaba_day_one_button.image = self.elphaba_day_one_hover

        # Placing Elphaba - Day 2 button
        self.elphaba_day_two = tk.PhotoImage(file="Designs/Elphaba_Day_Two.png")
        self.elphaba_day_two_button = tk.Button(self.root, image=self.elphaba_day_two, relief="raised")
        self.elphaba_day_two_button.image = self.elphaba_day_two
        self.elphaba_day_two_button.place(x=805, y=575, anchor="center")
        self.elphaba_day_two_hover = tk.PhotoImage(file="Designs/Elphaba_Day_Two_Hover.png")
        self.elphaba_day_two_button.bind("<Enter>", self.on_hover_elphaba_two)
        self.elphaba_day_two_button.bind("<Leave>", self.on_leave_elphaba_two)
        self.elphaba_day_two_button.image = self.elphaba_day_two_hover

        # Placing return button
        self.go_back = tk.PhotoImage(file="Designs/Catalogue_Back.png")
        self.go_back_button = tk.Button(self.root, image=self.go_back, relief="raised", command=self.open_title) # Call function that opens main menu
        self.go_back_button.image = self.go_back
        self.go_back_button.place(x=850, y= 630)
        self.go_back_hover = tk.PhotoImage(file="Designs/Catalogue_Back_Hover.png")
        self.go_back_button.bind("<Enter>", self.on_hover_back)
        self.go_back_button.bind("<Leave>", self.on_leave_back)
        self.go_back_button.image = self.go_back_hover

    # Series of functions for the hover effects for each button
    def on_hover_glinda_one(self, event):
        self.glinda_day_one_button.config(image=self.glinda_day_one_hover)

    def on_leave_glinda_one(self, event):
        self.glinda_day_one_button.config(image=self.glinda_day_one)

    def on_hover_glinda_two(self, event):
        self.glinda_day_two_button.config(image=self.glinda_day_two_hover)

    def on_leave_glinda_two(self, event):
        self.glinda_day_two_button.config(image=self.glinda_day_two)

    def on_hover_elphaba_one(self, event):
        self.elphaba_day_one_button.config(image=self.elphaba_day_one_hover)
    
    def on_leave_elphaba_one(self, event):
        self.elphaba_day_one_button.config(image=self.elphaba_day_one)

    def on_hover_elphaba_two(self, event):
        self.elphaba_day_two_button.config(image=self.elphaba_day_two_hover)

    def on_leave_elphaba_two(self, event):
        self.elphaba_day_two_button.config(image=self.elphaba_day_two)

    def on_hover_back(self, event):
        self.go_back_button.config(image=self.go_back_hover)
    
    def on_leave_back(self, event):
        self.go_back_button.config(image=self.go_back)

    # Function for opening the main menu
    def open_title(self):
        from tix_master import TixMaster
        self.catalogue_title_label.place_forget()
        TixMaster(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConcertCatalogue(root)
    root.mainloop()