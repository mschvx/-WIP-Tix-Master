# Importing necessary libraries
import tkinter as tk

# Main class for Tix Master title page
class TixMaster:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Tix Master")
        self.root.configure(bg="#d9e2f1")

        # Placing the main design of the title page
        self.main_title = tk.PhotoImage(file="Designs/Main_Title.png")
        self.main_title_label = tk.Label(self.root, image=self.main_title, bg="#d9e2f1")
        self.main_title_label.image = self.main_title
        self.main_title_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Placing the start button 
        self.start = tk.PhotoImage(file="Designs/Start_Button.png")
        self.start_button = tk.Button(self.root, image=self.start, relief="raised", command=self.open_catalogue) # Call function that opens catalogue
        self.start_button.image = self.start
        self.start_button.place(x=500, y=500, anchor="center")
        self.start_hover = tk.PhotoImage(file="Designs/Start_Button_Hover.png")
        self.start_button.bind("<Enter>", self.on_hover_start)
        self.start_button.bind("<Leave>", self.on_leave_start)
        self.start_button.image = self.start_hover

        # Placing the exit button
        self.exit = tk.PhotoImage(file="Designs/Exit_Button.png")
        self.exit_button = tk.Button(self.root, image=self.exit, relief="raised", command=self.root.quit) # Built-in command for exiting the window
        self.exit_button.image = self.exit
        self.exit_button.place(x=500, y=560, anchor="center")
        self.exit_hover = tk.PhotoImage(file="Designs/Exit_Button_Hover.png")
        self.exit_button.bind("<Enter>", self.on_hover_exit)
        self.exit_button.bind("<Leave>", self.on_leave_exit)
        self.exit_button.image = self.exit_hover

        # Placing the settings button
        self.settings = tk.PhotoImage(file="Designs/Settings_Button.png")
        self.settings_button = tk.Button(self.root, image=self.settings, relief="raised", command=self.open_settings) # Call function that opens settings
        self.settings_button.image = self.settings
        self.settings_button.place(x=850, y= 610)
        self.settings_hover = tk.PhotoImage(file="Designs/Settings_Button_Hover.png")
        self.settings_button.bind("<Enter>", self.on_hover_settings)
        self.settings_button.bind("<Leave>", self.on_leave_settings)
        self.settings_button.image = self.settings_hover

    # Series of functions for the hover effects for each button
    def on_hover_start(self, event):
        self.start_button.config(image=self.start_hover)

    def on_leave_start(self, event):
        self.start_button.config(image=self.start)

    def on_hover_exit(self, event):
        self.exit_button.config(image=self.exit_hover)

    def on_leave_exit(self, event):
        self.exit_button.config(image=self.exit)

    def on_hover_settings(self, event):
        self.settings_button.config(image=self.settings_hover)

    def on_leave_settings(self, event):
        self.settings_button.config(image=self.settings)

    # Function for opening the catalogue page
    def open_catalogue(self):
        from concert_catalogue import ConcertCatalogue
        self.main_title_label.place_forget()
        ConcertCatalogue(self.root)

    # Function for opening the settings page
    def open_settings(self):
        from tix_settings import TixSettings
        self.main_title_label.place_forget()
        TixSettings(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = TixMaster(root)
    root.mainloop()
