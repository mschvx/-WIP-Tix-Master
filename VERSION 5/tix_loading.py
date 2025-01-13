# Importing necessary libraries
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import random

# Main class for loading page
class TixLoading:
    # Setting up basic properties of the window
    def __init__(self, root, queue_number, selected_concert):
        self.root = root
        self.queue_number = queue_number
        self.selected_concert = selected_concert 
        self.root.geometry("1000x700")
        self.root.resizable(False, False)
        self.root.title("Loading...")
        self.root.configure(bg="#d9e2f1")

        # Initializing some necessary variables and putting the queues in a list for pop and delete
        self.queue_list = []
        self.current_queue = 1
        # Adding the previous queues to a list
        for i in range(self.queue_number):
            self.queue_list.append(self.current_queue)
            self.current_queue += 1

        # Dictionary variable where numbers will be added later to a corresponding seat number
        self.seating_arrangement = {
            1: None, 2: None, 3: None,
            4: None, 5: None, 6: None,
            7: None, 8: None, 9: None,
            10: None, 11: None, 12: None,
            13: None, 14: None, 15: None,
            16: None, 17: None, 18: None,
            19: None, 20: None, 21: None,
            22: None, 23: None, 24: None,
            25: None, 26: None, 27: None,
            28: None, 29: None, 30: None,
            31: None, 32: None, 33: None,
            34: None, 35: None, 36: None,
            37: None, 38: None, 39: None,
            40: None
        }

        # Placing the main design of the loading page
        self.loading_title = tk.PhotoImage(file="Designs/Loading/Loading_Screen.png")
        self.loading_title_label = tk.Label(self.root, image=self.loading_title, bg="#d9e2f1")
        self.loading_title_label.image = self.loading_title
        self.loading_title_label.place(x=0, y=0, relwidth=1, relheight=1)

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
        self.bar['value'] = 0

        # Placing the butterfly that moves along the loading bar
        self.butterfly = Image.open("Designs/Loading/Loading_Butterfly.png")
        self.butterfly_image = ImageTk.PhotoImage(self.butterfly)
        self.butterfly_id = self.loading_canvas.create_image(100, 265, anchor="center", image=self.butterfly_image)

        # Placing the percent below the loading bar
        self.loading_percent = tk.Label(self.root, text="0%", bd=1, font=("Helvetica", 20), bg="#798ec4", fg="#d9e2f1", relief="raised")
        self.loading_percent.place(x=500, y=400)

        # Placing queue line message below the loading bar
        self.queue_message = self.loading_canvas.create_text(500, 470, text=f"Your line number is {len(self.queue_list)}", font=("Helvetica", 20, "bold"), fill="#151c4c")

        # Start the loading process
        self.loading()

    # Function for loading title animation
    def animate_loading_title(self):
        # Deletes the previous frame
        if self.current_loading_id is not None:
            self.loading_canvas.delete(self.current_loading_id)
        # Logic for moving the animation
        self.current_loading_id = self.loading_canvas.create_image(500, 80, anchor="center", image=self.loading_images[self.current_loading_image])
        self.current_loading_image = (self.current_loading_image + 1) % len(self.loading_images)
        self.root.after(500, self.animate_loading_title)

    # Function for dequeue
    def dequeue(self):
        if self.queue_list:
            self.queue_list.pop(0)  # Remove the first element from the queue
        return self.queue_list
    
    # Function for the loading bar
    def loading(self):
        # Assigns a random empty seat with True
        if self.queue_list:
            assigned = False
            # Also checks in case the random number generates a filled seat
            while not assigned:
                assign_seat_number = random.randint(1, 40)
                if self.seating_arrangement[assign_seat_number] is None:
                    self.seating_arrangement[assign_seat_number] = True
                    # Saves the seats in a file (will be used for the concert seats proper)
                    with open("assigned_seats.dat", "w") as assignedSeats:
                        assignedSeats.write(str(self.seating_arrangement))
                    assigned = True
            self.dequeue()
            self.bar['value'] += 100 / self.queue_number  # Update the progress bar
            self.update_butterfly_position()  # Update butterfly position
            self.update_percent(f"{int(self.bar['value'])}%")  # Update percent text
            self.update_line(f"Your line number is {len(self.queue_list)}")
            if len(self.queue_list) > 0:  # Continue loading if there are still items in the queue
                self.root.after(1000, self.loading)
            if len(self.queue_list) == 0:  # If loading is complete
                self.open_seat_layout()
            
    def update_butterfly_position(self):
            # Calculate the new position of the butterfly based on the progress bar's value
            new_x = 100 + (self.bar['value'] / 100) * 800
            self.loading_canvas.coords(self.butterfly_id, new_x, 265)

    # Series of functions that change the texts below the loading bar (percent and queue number)
    def update_percent(self, value):
        self.loading_percent.config(text=value)
        # Center the loading percent
        self.loading_percent.place(x=500 - self.loading_percent.winfo_reqwidth() // 2, y=400)

    def update_line(self, value):
        self.loading_canvas.itemconfig(self.queue_message, text=value)
        self.loading_canvas.coords(self.queue_message, 500, 470)

    # Function for tracking  which concert was selected
    def open_seat_layout(self):
        if self.selected_concert == "Elphaba Day 1":
            from seats_ed1 import ED1Layout
            self.loading_canvas.pack_forget()
            ED1Layout(self.root)

        if self.selected_concert == "Elphaba Day 2":
            from seats_ed2 import ED2Layout
            self.loading_canvas.pack_forget()
            ED2Layout(self.root)

        if self.selected_concert == "Glinda Day 1":
            from seats_gd1 import GD1Layout
            self.loading_canvas.pack_forget()
            GD1Layout(self.root)

        if self.selected_concert == "Glinda Day 2":
            from seats_gd2 import GD2Layout
            self.loading_canvas.pack_forget()
            GD2Layout(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = TixLoading(root, queue_number=10, selected_concert="Elphaba Day 1")
    root.mainloop()