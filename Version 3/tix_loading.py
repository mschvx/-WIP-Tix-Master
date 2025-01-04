# Importing necessary libraries
import tkinter as tk
import time
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk

# Main class for loading page
class TixLoading:

    # Setting up basic properties of the window
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Loading...")
        self.root.configure(bg="#d9e2f1")

        # Placing the main design of the loading page
        self.loading_title = tk.PhotoImage(file="Designs/Loading/Loading_Screen.png")

        # Initializing some elements for the animations
        self.loading_one = Image.open("Designs/Loading/Loading_1.png")
        self.loading_one_image = ImageTk.PhotoImage(self.loading_one)  
        self.loading_two = Image.open("Designs/Loading/Loading_2.png")
        self.loading_two_image = ImageTk.PhotoImage(self.loading_two) 
        self.loading_three = Image.open("Designs/Loading/Loading_3.png")
        self.loading_three_image = ImageTk.PhotoImage(self.loading_three)
        self.loading_canvas = tk.Canvas(self.root, width=1000, height=700)
        self.loading_canvas.pack()
        self.loading_canvas.create_image(0, 0, anchor="nw", image=self.loading_title)

        # Animation proper for the loading title above the page
        self.current_loading_image = 0 # Track current image in the list below
        self.loading_images = [self.loading_one_image, self.loading_two_image, self.loading_three_image]
        self.current_loading_id = None # Tracks whatever is the current image
        self.animate_loading_title()

        # Placing the loading bar
        style = Style()
        style.theme_use('default')
        style.configure("TProgressbar",
                        troughcolor='#798ec4',  # Background color
                        background='#151c4c')  # Color of the progress bar
        self.bar = Progressbar(orient=HORIZONTAL, length=800, style="TProgressbar", mode='determinate')
        self.bar.place(x=500, y=350, anchor="center", height=40)
        self.bar['value'] = 23

    # Function for loading title animation
    def animate_loading_title(self):
        # Deletes the previous frame
        if self.current_loading_id is not None:
            self.loading_canvas.delete(self.current_loading_id)
        # Logic for moving the animation
        self.current_loading_id = self.loading_canvas.create_image(500, 80, anchor="center", image=self.loading_images[self.current_loading_image])
        self.current_loading_image = (self.current_loading_image + 1) % len(self.loading_images)
        self.root.after(500, self.animate_loading_title)

if __name__ == "__main__":
    root = tk.Tk()
    app = TixLoading(root)
    root.mainloop()